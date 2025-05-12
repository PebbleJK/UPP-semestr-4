import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt
import pandas as pd
import pyqtgraph as pg

class PlotWindow(QWidget):
    def __init__(self, data, moving_avg, anomalies):
        super().__init__()
        self.setWindowTitle("Temperatura - wykres liniowy")
        self.resize(600, 400)

        plot_widget = pg.PlotWidget()
        plot_widget.setBackground('w')
        plot_widget.setTitle("Temperatura w czasie", color="black", size="16pt")
        plot_widget.setLabel('left', 'Temperatura (°C)', color='black')
        plot_widget.setLabel('bottom', 'Indeks (dni)', color='black')
        plot_widget.showGrid(x=True, y=True)

        y = data["temperature"].values
        avg = moving_avg
        anomalies_data = anomalies
        x = list(range(len(y)))

        plot_widget.plot(x, y, pen=pg.mkPen(color='r', width=2), symbol='o', symbolSize=4, symbolBrush='r', name='Temperatura')

        plot_widget.plot(x, avg, pen=pg.mkPen(color='b', width=2, style=QtCore.Qt.DashLine), name='Średnia krocząca')

        anomaly_indices = [i for i, val in enumerate(anomalies_data) if val == "ANOMALIA"]
        anomaly_values = [y[i] for i in anomaly_indices]
        plot_widget.plot(anomaly_indices, anomaly_values, pen=None, symbol='o', symbolBrush='g', symbolSize=8, name='Anomalie')

        layout = QVBoxLayout()
        layout.addWidget(plot_widget)
        self.setLayout(layout)


class RainBarChartWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Miesięczne opady")
        self.resize(600, 400)

        plot_widget = pg.PlotWidget()
        plot_widget.setBackground('w')
        plot_widget.setTitle("Suma opadów miesięcznie", color="black", size="14pt")
        plot_widget.setLabel('left', 'Suma opadów (mm)', color='black')
        plot_widget.setLabel('bottom', 'Miesiąc', color='black')
        plot_widget.showGrid(x=True, y=True)

        data["month"] = data["date"].dt.month
        monthly_rain = data.groupby("month")["precipitation"].sum()

        x = list(range(1, 13))
        y = [monthly_rain.get(m, 0) for m in x]

        bg = pg.BarGraphItem(x=x, height=y, width=0.6, brush='blue')
        plot_widget.addItem(bg)

        months = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        ticks = [(i, months[i - 1]) for i in x]
        plot_widget.getAxis('bottom').setTicks([ticks])

        layout = QVBoxLayout()
        layout.addWidget(plot_widget)
        self.setLayout(layout)


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        value = self._data.iloc[index.row(), index.column()]
        if role == Qt.DisplayRole:
            return str(value)
        if role == Qt.BackgroundRole and self._data.columns[index.column()] == "Anomalia":
            if value == "ANOMALIA":
                return QtGui.QColor("red")

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pogoda")
        self.resize(1200, 600)

        self.data = pd.read_csv("./Zajecia6/weather.csv", parse_dates=["date"])
        self.datadf = pd.DataFrame(self.data, columns=["date", "temperature", "humidity", "precipitation"])
        self.datadf = self.datadf.interpolate()

        self.datadf["Średnia krocząca"] = self.datadf["temperature"].rolling(window=3).mean().round(2) # Średnia krocząca z krokiem 3
        
        self.datadf["month"] = pd.to_datetime(self.datadf["date"]).dt.month
        monthly_stats = self.datadf.groupby("month")["temperature"].agg(["mean", "std"]).rename(columns={"mean": "m_mean", "std": "m_std"})
        self.datadf = self.datadf.join(monthly_stats, on="month")

        self.datadf["Anomalia (miesięczna)"] = self.datadf.apply(
            lambda row: "ANOMALIA" if abs(row["temperature"] - row["m_mean"]) > 2 * row["m_std"] else "-", axis=1
        )

        self.datadf["Data"] = pd.to_datetime(self.datadf["date"]).dt.strftime("%Y-%m-%d")
        self.datadf["Temperatura"] = self.datadf["temperature"]
        self.datadf["Wilgotność"] = self.datadf["humidity"]
        self.datadf["Opady"] = self.datadf["precipitation"]
        self.datadf["Średnia krocząca"] = self.datadf["Średnia krocząca"]
        self.datadf["Anomalia"] = self.datadf["Anomalia (miesięczna)"]

        self.datadf = self.datadf[["Data", "Temperatura", "Wilgotność", "Opady", "Średnia krocząca", "Anomalia"]]
        self.table = QtWidgets.QTableView()
        self.model = TableModel(self.datadf)
        self.table.setModel(self.model)
        self.table.setFixedWidth(700)

        self.corrTable = QtWidgets.QTableView()
        self.corrTable.setModel(TableModel(self.datadf[["Temperatura", "Wilgotność", "Opady"]].corr()))
        self.corrTable.setFixedHeight(150)
        self.corrTable.setFixedWidth(400)
        self.tempButton = QPushButton("Temperatura (wykres liniowy)")
        self.tempButton.clicked.connect(self.show_temp_plot)
        self.rainButton = QPushButton("Miesięczne opady (wykres słupkowy)")
        self.rainButton.clicked.connect(self.show_rain_chart)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.corrTable)
        rightLayout.addWidget(self.tempButton)
        rightLayout.addWidget(self.rainButton)

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(rightLayout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_temp_plot(self):
        moving_avg = self.datadf["Średnia krocząca"].values 
        anomalies = self.datadf["Anomalia"].values
        self.plot_window = PlotWindow(self.data, moving_avg, anomalies)
        self.plot_window.show()

    def show_rain_chart(self):
        self.rain_window = RainBarChartWindow(self.data)
        self.rain_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

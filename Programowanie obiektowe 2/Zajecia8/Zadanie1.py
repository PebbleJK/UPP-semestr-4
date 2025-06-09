import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QColorDialog

class PatternDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pattern Drawer")
        self.canvas_label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.canvas_label.setPixmap(canvas)
        self.setCentralWidget(self.canvas_label)

        # Panel narzędzi
        tools = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        tools.setLayout(layout)

        self.pattern_cb = QtWidgets.QComboBox()
        self.pattern_cb.addItems(["Kropki", "Pionowe linie", "Małe kółka"])
        layout.addWidget(self.pattern_cb)

        self.colors_spin = QtWidgets.QSpinBox()
        self.colors_spin.setRange(1, 3)
        layout.addWidget(self.colors_spin)

        self.color_buttons = []
        for i in range(3):
            btn = QtWidgets.QPushButton(f"Kolor {i+1}")
            btn.clicked.connect(self.choose_color_factory(i))
            btn.setEnabled(i == 0)
            self.color_buttons.append(btn)
            layout.addWidget(btn)

        self.draw_btn = QtWidgets.QPushButton("Narysuj")
        self.draw_btn.clicked.connect(self.draw_pattern)
        layout.addWidget(self.draw_btn)

        toolbar = QtWidgets.QToolBar()
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, toolbar)
        toolbar.addWidget(tools)


        self.selected_colors = [QtGui.QColor('black')] * 3
        self.colors_spin.valueChanged.connect(self.update_color_buttons)

    def choose_color_factory(self, idx):
        def choose_color():
            col = QColorDialog.getColor()
            if col.isValid():
                self.selected_colors[idx] = col
        return choose_color

    def update_color_buttons(self, count):
        for i, btn in enumerate(self.color_buttons):
            btn.setEnabled(i < count)

    def draw_pattern(self):
        pattern = self.pattern_cb.currentText()
        count = self.colors_spin.value()
        colors = self.selected_colors[:count]
        canvas = self.canvas_label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.fillRect(canvas.rect(), QtGui.QBrush(Qt.GlobalColor.white))
        
        if pattern == "Kropki":
            for x in range(10, canvas.width(), 20):
                for y in range(10, canvas.height(), 20):
                    pen = QtGui.QPen(colors[(x//20 + y//20) % count])
                    painter.setPen(pen)
                    painter.drawPoint(x, y)

        elif pattern == "Pionowe linie":
            for i, x in enumerate(range(0, canvas.width(), 20)):
                pen = QtGui.QPen(colors[i % count], 2)
                painter.setPen(pen)
                painter.drawLine(x, 0, x, canvas.height())

        elif pattern == "Małe kółka":
            r = 5
            for i, x in enumerate(range(20, canvas.width(), 30)):
                for j, y in enumerate(range(20, canvas.height(), 30)):
                    pen = QtGui.QPen(colors[(i+j) % count])
                    painter.setPen(pen)
                    painter.drawEllipse(x - r, y - r, 2*r, 2*r)

        painter.end()
        self.canvas_label.setPixmap(canvas)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = PatternDrawer()
    win.show()
    sys.exit(app.exec())

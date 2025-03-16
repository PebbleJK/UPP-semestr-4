from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPainter, QPen, QMouseEvent
from PySide6.QtCore import Qt, QPoint
import sys

class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.drawing = False
        self.last_point = None
        self.lines = []

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            print(self.lines)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drawing and self.last_point is not None:
            self.lines.append((self.last_point, event.pos()))
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            self.last_point = None

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        for line in self.lines:
            painter.drawLine(line[0], line[1])

    def clearCanvas(self):
        self.lines = []
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prosty Paint")
        self.paint_widget = PaintWidget()
        self.setCentralWidget(self.paint_widget)
        
        self.clear_button = QPushButton("Wyczyść", self)
        self.clear_button.setGeometry(10, 10, 100, 30)
        self.clear_button.clicked.connect(self.paint_widget.clearCanvas)
        self.clear_button.raise_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem, QLineEdit, QFileDialog, QGraphicsEllipseItem, QGraphicsPolygonItem
from PySide6.QtGui import QBrush, QPen, QImage, QPainter, QPolygonF
from PySide6.QtCore import Qt, QPointF

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        # Zmienne do rysowania
        self.colors = [Qt.red, Qt.blue, Qt.green]
        self.currentZ = 0

        # Guziki
        self.rectangleButton = QPushButton("Prostokąt")
        self.triangleButton = QPushButton("Trójkąt")
        self.ellipseButton = QPushButton("Elipsa")
        self.upButton = QPushButton("Góra")
        self.downButton = QPushButton("Dół")
        self.deleteButton = QPushButton("Usuń")
        self.saveButton = QPushButton("Zapisz(.png)")

        self.rectangleButton.clicked.connect(self.addRectangle)
        self.triangleButton.clicked.connect(self.addTriangle)
        self.ellipseButton.clicked.connect(self.addEllipse)

        self.upButton.clicked.connect(self.raiseItem)
        self.downButton.clicked.connect(self.lowerItem)
        self.deleteButton.clicked.connect(self.deleteItem)
        self.saveButton.clicked.connect(self.saveAsPng)

        # Inputy
        self.figureWidth = QLineEdit()
        self.figureWidth.setPlaceholderText("Szerokość")
        self.figureHeight = QLineEdit()
        self.figureHeight.setPlaceholderText("Wysokość")
        self.figureX = QLineEdit()
        self.figureX.setPlaceholderText("x")
        self.figureY = QLineEdit()
        self.figureY.setPlaceholderText("y")
        self.figureColor = QLineEdit()
        self.figureColor.setPlaceholderText("Kolor (0-2)")



        # Scena
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0 , 500, 500)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(520,520)

        # Layouty
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.rectangleButton)
        buttonLayout.addWidget(self.triangleButton)
        buttonLayout.addWidget(self.ellipseButton)
        buttonLayout.addWidget(self.upButton)
        buttonLayout.addWidget(self.downButton)
        buttonLayout.addWidget(self.deleteButton)
        buttonLayout.addWidget(self.saveButton)

        lineEditLayout = QHBoxLayout()
        lineEditLayout.addWidget(self.figureWidth)
        lineEditLayout.addWidget(self.figureHeight)
        lineEditLayout.addWidget(self.figureX)
        lineEditLayout.addWidget(self.figureY)
        lineEditLayout.addWidget(self.figureColor)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(lineEditLayout)
        mainLayout.addWidget(self.view)

        centralWidget = QWidget()  
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)  


    def addRectangle(self):
        width = float(self.figureWidth.text())
        height = float(self.figureHeight.text())
        x = float(self.figureX.text())
        y = float(self.figureY.text())
        rectangle = QGraphicsRectItem(x, y , width, height)
        self.brush = self.colors[int(self.figureColor.text())]
        rectangle.setBrush(self.brush)
        rectangle.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        rectangle.setZValue(self.currentZ)
        self.currentZ += 1
        self.scene.addItem(rectangle)

    def addTriangle(self):
        width = float(self.figureWidth.text())
        height = float(self.figureHeight.text())
        x = float(self.figureX.text())
        y = float(self.figureY.text())
        brush = self.colors[int(self.figureColor.text())]

        # Wierzchołki trójkąta równoramiennego
        points = [
            QPointF(x + width / 2, y),           # góra
            QPointF(x, y + height),              # lewy dół
            QPointF(x + width, y + height)       # prawy dół
        ]

        triangle = QGraphicsPolygonItem(QPolygonF(points))
        triangle.setBrush(brush)
        triangle.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        triangle.setZValue(self.currentZ)
        self.currentZ += 1
        self.scene.addItem(triangle)

    def addEllipse(self):
        width = float(self.figureWidth.text())
        height = float(self.figureHeight.text())
        x = float(self.figureX.text())
        y = float(self.figureY.text())
        ellipse = QGraphicsEllipseItem(x, y , width, height)
        self.brush = self.colors[int(self.figureColor.text())]
        ellipse.setBrush(self.brush)
        ellipse.setFlag(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        ellipse.setZValue(self.currentZ)
        self.currentZ += 1
        self.scene.addItem(ellipse)


    # inne figury

    def raiseItem(self):
        selected = self.scene.selectedItems()
        if not selected:
            return
        item = selected[0]
        
        # Znajdź maksymalny z-index w scenie
        max_z = max((i.zValue() for i in self.scene.items()), default=0)
        item.setZValue(max_z + 1)

    def lowerItem(self):
        selected = self.scene.selectedItems()
        if not selected:
            return
        item = selected[0]

        # Znajdź minimalny z-index w scenie
        min_z = min((i.zValue() for i in self.scene.items()), default=0)
        item.setZValue(min_z - 1)

    def deleteItem(self):
        selected_items = self.scene.selectedItems()
        for item in selected_items:
            self.scene.removeItem(item)
    
    def saveAsPng(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz jako PNG", "", "PNG Files (*.png)")
        if not file_path:
            return

        rect = self.scene.sceneRect()
        image = QImage(int(rect.width()), int(rect.height()), QImage.Format_ARGB32)
        image.fill(Qt.white)

        painter = QPainter(image)
        self.scene.render(painter)
        painter.end()

        image.save(file_path)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


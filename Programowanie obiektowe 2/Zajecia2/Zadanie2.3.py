import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    centralWidget = QWidget()
    self.setCentralWidget(centralWidget)

    self.wynik = 0
    self.wynikLabel = QLabel(f"Wynik: {self.wynik}")


    layout = QGridLayout()
    layout.addWidget(self.wynikLabel, 1, 1)

    addButton = QPushButton("+1")
    addButton.clicked.connect(self.addOne)
    layout.addWidget(addButton, 0, 0)

    substractButton = QPushButton("-1")
    substractButton.clicked.connect(self.substractOne)
    layout.addWidget(substractButton, 0, 2)

    multiplyButton = QPushButton("x2")
    multiplyButton.clicked.connect(self.doubleResult)
    layout.addWidget(multiplyButton, 2, 0)

    divideButton = QPushButton("/2")
    divideButton.clicked.connect(self.halveResult)
    layout.addWidget(divideButton, 2, 2)

    centralWidget.setLayout(layout)

  def addOne(self):
    self.wynik += 1
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def substractOne(self):
    self.wynik -= 1
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def doubleResult(self):
    self.wynik *= 2
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def halveResult(self):
    self.wynik /= 2
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())


if __name__ == "__main__":
  main()


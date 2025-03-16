import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QWidget


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    centralWidget = QWidget()
    self.setCentralWidget(centralWidget)

    self.wynik = 0
    self.wynikLabel = QLabel(f"Wynik: {self.wynik}")


    layout = QHBoxLayout()
    layout.addWidget(self.wynikLabel)

    addButton = QPushButton("+1")
    addButton.clicked.connect(self.addOne)
    layout.addWidget(addButton)

    substractButton = QPushButton("-1")
    substractButton.clicked.connect(self.substractOne)
    layout.addWidget(substractButton)

    multiplyButton = QPushButton("x2")
    multiplyButton.clicked.connect(self.doubleResult)
    layout.addWidget(multiplyButton)

    divideButton = QPushButton("/2")
    divideButton.clicked.connect(self.halveResult)
    layout.addWidget(divideButton)

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


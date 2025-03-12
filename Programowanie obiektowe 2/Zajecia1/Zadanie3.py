import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Slot
from PySide6.QtGui import QDoubleValidator

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Zmiana stylu Qlabel
    self.setGeometry(100, 100, 400, 400)
    self.label = QLabel("Jakiś fajny tekst", self)
    self.label.setGeometry(20,20,200,50)
    styleButton = QPushButton("Zmień styl tekstu", self)
    styleButton.setGeometry(220, 30, 100, 30)
    styleButton.clicked.connect(self.changeLabel)

    # Czyszczenie pola input
    self.clearInput = QLineEdit(self)
    self.clearInput.setGeometry(20, 80, 100, 30)
    clearButton = QPushButton("Wyczyść", self)
    clearButton.setGeometry(120, 80, 100, 30)
    clearButton.clicked.connect(self.clearInput.clear)

    # Kalkulator
    self.number1 = QLineEdit(self)
    self.number1.setGeometry(20, 150, 50, 20)
    self.number2 = QLineEdit(self)
    self.number2.setGeometry(80, 150, 50, 20)
    self.number1.setValidator(QDoubleValidator()) # Widzę że te walidatory nawet nie pozwalają wpisać liter
    self.number2.setValidator(QDoubleValidator())

    addButton = QPushButton("+", self)
    addButton.setGeometry(20, 180, 20, 20)
    addButton.clicked.connect(self.add)

    subButton = QPushButton("-", self)
    subButton.setGeometry(50, 180, 20, 20)
    subButton.clicked.connect(self.sub)

    multiplyButton = QPushButton("*", self)
    multiplyButton.setGeometry(80, 180, 20, 20)
    multiplyButton.clicked.connect(self.multiply)

    divideButton = QPushButton("/", self)
    divideButton.setGeometry(110, 180, 20, 20)
    divideButton.clicked.connect(self.divide)


    self.result = QLabel("Wynik: ", self)
    self.result.setGeometry(20, 200, 200, 20)

  def changeLabel(self):
    self.label.setStyleSheet(
      "background-color: red;"
      "font-size: 24px;")

  def isEmpty(self, input):
    if input == "":
      return True
    else:
      return False

  def add(self):
    num1 = self.number1.text()
    num2 = self.number2.text()
    if self.isEmpty(num1) or self.isEmpty(num2):
      self.result.setText("Wprowadź obie wartości")
    else:
      self.result.setText(f"Wynik: {float(num1) + float(num2)}")

  def sub(self):
    num1 = self.number1.text()
    num2 = self.number2.text()
    if self.isEmpty(num1) or self.isEmpty(num2):
      self.result.setText("Wprowadź obie wartości")
    else:
      self.result.setText(f"Wynik: {float(num1) - float(num2)}")

  def multiply(self):
    num1 = self.number1.text()
    num2 = self.number2.text()
    if self.isEmpty(num1) or self.isEmpty(num2):
      self.result.setText("Wprowadź obie wartości")
    else:
      self.result.setText(f"Wynik: {float(num1) * float(num2)}")

  def divide(self):
    num1 = self.number1.text()
    num2 = self.number2.text()
    if self.isEmpty(num1) or self.isEmpty(num2):
      self.result.setText("Wprowadź obie wartości")
    elif float(num2) != 0:
      self.result.setText(f"Wynik: {float(num1) / float(num2)}")
    else:
      self.result.setText("Nie dziel przez 0!")

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()


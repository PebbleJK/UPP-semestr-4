from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("My App")
    self.button_is_checked = True
    #self.setFixedSize(QSize(400,400)) zablokowanie wymierów okienka
    #.setMinimumSize() .setMaximumSize()
    
    self.button = QPushButton("Press Me!")
    self.button.setCheckable(True)
    self.button.setChecked(self.button_is_checked)
    self.button.clicked.connect(self.the_button_was_clicked)
    self.button.clicked.connect(self.the_button_was_toggled)

    self.setCentralWidget(self.button)

  def the_button_was_clicked(self):
    print("Clicked!")

  def the_button_was_toggled(self, checked):
    self.button_is_checked = self.button.isChecked()
    print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

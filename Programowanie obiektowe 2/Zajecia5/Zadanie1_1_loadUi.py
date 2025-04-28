from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

class MainWindow(QDialog):  # <-- dziedzicz z QDialog, bo w .ui jest QDialog
    def __init__(self):
        super().__init__()
        uic.loadUi("Zadanie1_1_form.ui", self)  # <-- wczytujemy plik .ui bezpośrednio do self

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
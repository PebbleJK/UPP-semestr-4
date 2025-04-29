from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

class MainWindow(QDialog):  # <-- dziedzicz z QDialog, bo w .ui jest QDialog
    def __init__(self):
        super().__init__()
        uic.loadUi(".\Zajecia5\Zadanie1_1_form.ui", self)  # <-- wczytujemy plik .ui bezpośrednio do self

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
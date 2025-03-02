import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
text = "Jakiś link"
label = QLabel("Jakiś link", margin = 48)
label.set
label.setStyleSheet("color: red;")
label.setStyleSheet("color: red; background-color: yellow;")
#QVboxlayout
label.show()
app.exec()

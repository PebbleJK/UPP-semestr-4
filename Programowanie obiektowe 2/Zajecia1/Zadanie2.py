import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt

# Spersonalizowany QLabel do klikania
class ClickableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        self.setText("Działa")

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Zadanie2")
    self.setGeometry(400, 200, 500, 600)

    # Losowy label
    self.label1 = QLabel("Jakiś label", self)
    self.label1.setFont(QFont("Arial",30))
    self.label1.setGeometry(20, 20, 300, 100)
    self.label1.setStyleSheet(
      "color: red;"
      "background-color: yellow;")
    self.label1.setAlignment(Qt.AlignTop) # Wyrównanie 1
    
    # Label do klikania
    self.label2 = ClickableLabel("Kliknij na mnie", self);
    self.label2.setFont(QFont("Arial",30))
    self.label2.setGeometry(20, 130, 400, 100)
    self.label2.setStyleSheet(
      "color: blue;"
      "background-color: yellow;")
    self.label2.setAlignment(Qt.AlignCenter) # Wyrównanie 2
    
    # Link
    self.label3 = QLabel('<a href="https://mateusz-jarczynski.pl/up/">Link </a>', self)
    self.label3.setFont(QFont("Arial",30))
    self.label3.setGeometry(20, 230, 400, 100)
    self.label3.setStyleSheet(
      "background-color: cyan;")
    self.label3.setTextFormat(Qt.RichText) # Pozwala na interpretacje tekstu jako html
    self.label3.setOpenExternalLinks(True) # Pozwala na otwieranie linków
    self.label3.setAlignment(Qt.AlignRight | Qt.AlignVCenter) # Wyrównanie 3

    #Obrazek
    self.imageLabel = QLabel(self)
    self.imageLabel.setGeometry(20, 330, 150, 150)
    self.pixmap = QPixmap("ja.png") 
    self.imageLabel.setPixmap(self.pixmap)
    self.imageLabel.setScaledContents(True) # Skalowanie

    #Obrazek2
    self.imageLabe2 = QLabel(self)
    self.imageLabe2.setGeometry(220, 330, 200, 200)
    self.pixmap = QPixmap("ja.png") 
    self.imageLabe2.setPixmap(self.pixmap)
    self.imageLabe2.setScaledContents(True) # Skalowanie




def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())


if __name__ == "__main__":
  main()


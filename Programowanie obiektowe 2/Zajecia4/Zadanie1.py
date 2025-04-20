import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Przeglądarka obrazów")
        self.resize(600, 400)

        self.image_label = QLabel("Brak załadowanego obrazu")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.load_button = QPushButton("Wczytaj obraz")
        self.save_button = QPushButton("Zapisz jako...")

        self.load_button.clicked.connect(self.load_image)
        self.save_button.clicked.connect(self.save_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

        self.current_pixmap = None

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz plik graficzny",
            "",
            "Obrazy (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_name:
            pixmap = QPixmap(file_name)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap)
                self.current_pixmap = pixmap
            else:
                self.image_label.setText("Nie udało się wczytać obrazu.")

    def save_image(self):
        if self.current_pixmap is None:
            self.image_label.setText("Najpierw wczytaj obraz.")
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Zapisz obraz jako",
            "",
            "Obrazy (*.png *.jpg *.bmp)"
        )
        if file_name:
            #print(file_name)
            #extension = file_name.split('.')[-1].lower()
            #if extension in ['jpg', 'jpeg', 'png', 'bmp']:
            self.current_pixmap.save(file_name)
                #self.current_pixmap.save(file_name, format=extension.upper())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())

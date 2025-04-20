import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QFileDialog, QCheckBox
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QRect


class PersistentImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistent Image Viewer")
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setGeometry(600, 100, 300, 300)

        self.image_label = QLabel("Brak obrazka.")
        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def show_image(self, pixmap: QPixmap):
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaled(280, 280, Qt.KeepAspectRatio))
            self.show()
        else:
            self.image_label.setText("Nie można załadować obrazka.")
            self.hide()

    def clear_image(self):
        self.image_label.clear()
        self.image_label.setText("Brak obrazka.")
        self.hide()


class OnDemandWindow(QWidget):
    def __init__(self, apply_transform_callback):
        super().__init__()
        self.setWindowTitle("Ustawienia obrazu")
        self.setGeometry(450, 100, 300, 250)

        self.apply_transform_callback = apply_transform_callback

        self.grayscale_cb = QCheckBox("Skala szarości")
        self.mirror_cb = QCheckBox("Odbicie lustrzane")
        self.crop_cb = QCheckBox("Kadrowanie (50x50)")
        self.resize_cb = QCheckBox("Przeskalowanie (100x100)")

        self.apply_btn = QPushButton("Zastosuj")
        self.apply_btn.clicked.connect(self.apply_transform_callback)

        layout = QVBoxLayout()
        layout.addWidget(self.grayscale_cb)
        layout.addWidget(self.mirror_cb)
        layout.addWidget(self.crop_cb)
        layout.addWidget(self.resize_cb)
        layout.addStretch()
        layout.addWidget(self.apply_btn)
        self.setLayout(layout)

    def get_settings(self):
        return {
            "grayscale": self.grayscale_cb.isChecked(),
            "mirror": self.mirror_cb.isChecked(),
            "crop": self.crop_cb.isChecked(),
            "resize": self.resize_cb.isChecked(),
        }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Główne Okno")
        self.setGeometry(100, 100, 400, 200)

        self.image_path = None
        self.original_image = None

        self.persistent_window = PersistentImageWindow()
        self.on_demand_window = OnDemandWindow(self.apply_image_transform)

        self.open_on_demand_btn = QPushButton("Ustawienia obrazu")
        self.open_on_demand_btn.clicked.connect(self.on_demand_window.show)

        self.load_image_btn = QPushButton("Wybierz obrazek")
        self.load_image_btn.clicked.connect(self.load_image)

        self.clear_image_btn = QPushButton("Usuń obrazek")
        self.clear_image_btn.clicked.connect(self.clear_image)

        layout = QVBoxLayout()
        layout.addWidget(self.open_on_demand_btn)
        layout.addWidget(self.load_image_btn)
        layout.addWidget(self.clear_image_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Wybierz obrazek", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.image_path = file_path
            self.original_image = QImage(file_path)
            self.apply_image_transform()

    def apply_image_transform(self):
        if not self.original_image:
            return

        image = self.original_image.copy()
        settings = self.on_demand_window.get_settings()

        # Skala szarości
        if settings["grayscale"]:
            image = image.convertToFormat(QImage.Format_Grayscale8)

        # Odbicie lustrzane
        if settings["mirror"]:
            image = image.mirrored(True, False)

        # Kadrowanie (crop)
        if settings["crop"]:
            rect = QRect(0, 0, 50, 50)
            image = image.copy(rect)

        # Przeskalowanie
        if settings["resize"]:
            image = image.scaled(100, 100, Qt.KeepAspectRatio)

        pixmap = QPixmap.fromImage(image)
        self.persistent_window.show_image(pixmap)

    def clear_image(self):
        self.original_image = None
        self.image_path = None
        self.persistent_window.clear_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

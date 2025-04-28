from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox
)
import os
import zipfile
import csv
import sys

class FileOperationsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operacje na plikach")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Przyciski
        self.list_files_btn = QPushButton("Wylistuj pliki w folderze")
        self.zip_files_btn = QPushButton("Spakuj pliki do ZIP")
        self.import_csv_btn = QPushButton("Importuj CSV do tabeli")

        self.layout.addWidget(self.list_files_btn)
        self.layout.addWidget(self.zip_files_btn)
        self.layout.addWidget(self.import_csv_btn)

        # Tabela
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Powiązanie przycisków z funkcjami
        self.list_files_btn.clicked.connect(self.list_files)
        self.zip_files_btn.clicked.connect(self.zip_files)
        self.import_csv_btn.clicked.connect(self.import_csv)

    def list_files(self):
        folder = QFileDialog.getExistingDirectory(self, "Wybierz folder")
        if folder:
            files = os.listdir(folder)
            self.table.setRowCount(len(files))
            self.table.setColumnCount(1)
            self.table.setHorizontalHeaderLabels(["Pliki"])
            for i, file in enumerate(files):
                self.table.setItem(i, 0, QTableWidgetItem(file))

    def zip_files(self):
        folder = QFileDialog.getExistingDirectory(self, "Wybierz folder do spakowania")
        if folder:
            save_path, _ = QFileDialog.getSaveFileName(self, "Zapisz ZIP jako", filter="ZIP files (*.zip)")
            if save_path:
                if not save_path.endswith('.zip'):
                    save_path += '.zip'
                try:
                    with zipfile.ZipFile(save_path, 'w') as zipf:
                        for root, _, files in os.walk(folder):
                            for file in files:
                                filepath = os.path.join(root, file)
                                arcname = os.path.relpath(filepath, folder)
                                zipf.write(filepath, arcname)
                    QMessageBox.information(self, "Sukces", f"Folder został spakowany do {save_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Błąd", str(e))

    def import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik CSV", filter="CSV files (*.csv)")
        if file_path:
            try:
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    data = list(reader)

                    if data:
                        self.table.setRowCount(len(data) - 1)  # pierwsza linia - nagłówki
                        self.table.setColumnCount(len(data[0]))
                        self.table.setHorizontalHeaderLabels(data[0])

                        for row_idx, row_data in enumerate(data[1:]):
                            for col_idx, item in enumerate(row_data):
                                self.table.setItem(row_idx, col_idx, QTableWidgetItem(item))
            except Exception as e:
                QMessageBox.critical(self, "Błąd", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOperationsApp()
    window.show()
    sys.exit(app.exec())

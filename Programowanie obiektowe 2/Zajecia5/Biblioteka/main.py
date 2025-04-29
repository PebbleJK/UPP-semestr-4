import sys
import os
import datetime
from dataclasses import dataclass
from typing import List, Optional

from PyQt6 import QtWidgets, uic, QtGui, QtCore
from PyQt6.QtCore import Qt


@dataclass
class Book:
    title: str
    author: str
    genre: str
    is_borrowed: bool = False
    borrower_name: Optional[str] = None
    borrowed_date: Optional[datetime.date] = None

    def is_overdue(self):
        if not self.is_borrowed or not self.borrowed_date:
            return False
        return (datetime.date.today() - self.borrowed_date).days > 14


class BookModel(QtCore.QAbstractTableModel):
    headers = ["Tytuł", "Autor", "Gatunek", "Status", "Wypożyczający", "Data"]

    def __init__(self, books: List[Book]):
        super().__init__()
        self.books = books
        self.filtered_books = books.copy()
        self.filter_mode = "Wszystkie"
        self.sort_column = 0
        self.sort_order = Qt.SortOrder.AscendingOrder

    def rowCount(self, index):
        return len(self.filtered_books)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        book = self.filtered_books[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            return [
                book.title,
                book.author,
                book.genre,
                "Wypożyczona" if book.is_borrowed else "Dostępna",
                book.borrower_name or "",
                book.borrowed_date.strftime("%Y-%m-%d") if book.borrowed_date else ""
            ][col]

        if role == Qt.ItemDataRole.DecorationRole and col == 3:
            icon_path = "zajecia5/Biblioteka/icons/borrowed.png" if book.is_borrowed else "zajecia5/Biblioteka/icons/available.png"
            return QtGui.QIcon(icon_path)

        if role == Qt.ItemDataRole.BackgroundRole and book.is_overdue():
            return QtGui.QColor("red")

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.headers[section]

    def sort(self, column, order):
        self.sort_column = column
        self.sort_order = order
        self.layoutAboutToBeChanged.emit()
        key_funcs = [
            lambda b: b.title,
            lambda b: b.author,
            lambda b: b.genre,
            lambda b: b.is_borrowed,
            lambda b: b.borrower_name or "",
            lambda b: b.borrowed_date or datetime.date.min,
        ]
        self.filtered_books.sort(key=key_funcs[column], reverse=order == Qt.SortOrder.DescendingOrder)
        self.layoutChanged.emit()

    def filter_books(self, mode):
        self.layoutAboutToBeChanged.emit()
        self.filter_mode = mode
        if mode == "Dostępne":
            self.filtered_books = [b for b in self.books if not b.is_borrowed]
        elif mode == "Wypożyczone":
            self.filtered_books = [b for b in self.books if b.is_borrowed]
        else:
            self.filtered_books = self.books.copy()
        self.sort(self.sort_column, self.sort_order)
        self.layoutChanged.emit()

    def get_book(self, row):
        return self.filtered_books[row]

    def update_model(self):
        self.filter_books(self.filter_mode)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("zajecia5/Biblioteka/biblioteka.ui", self)
        self.model = BookModel(self.create_books())
        self.bookTable.setModel(self.model)
        self.bookTable.setSortingEnabled(True)

        self.filterCombo.currentTextChanged.connect(self.model.filter_books)
        self.borrowButton.clicked.connect(self.borrow_book)
        self.returnButton.clicked.connect(self.return_book)

        self.check_overdue_books()

    def create_books(self) -> List[Book]:
        return [
            Book("Wiedźmin", "Andrzej Sapkowski", "Fantasy"),
            Book("Lalka", "Bolesław Prus", "Powieść"),
            Book("Zbrodnia i kara", "Fiodor Dostojewski", "Klasyka", True, "Jan Kowalski", datetime.date.today() - datetime.timedelta(days=15)),
            Book("Hobbit", "J.R.R. Tolkien", "Fantasy", True, "Anna Nowak", datetime.date.today())
        ]

    def borrow_book(self):
        index = self.bookTable.currentIndex()
        if not index.isValid():
            return

        book = self.model.get_book(index.row())
        if book.is_borrowed:
            return

        name, ok = QtWidgets.QInputDialog.getText(self, "Wypożycz", "Imię i nazwisko:")
        if ok and name:
            book.is_borrowed = True
            book.borrower_name = name
            book.borrowed_date = datetime.date.today()
            self.model.update_model()

    def return_book(self):
        index = self.bookTable.currentIndex()
        if not index.isValid():
            return

        book = self.model.get_book(index.row())
        book.is_borrowed = False
        book.borrower_name = None
        book.borrowed_date = None
        self.model.update_model()

    def check_overdue_books(self):
        overdue = [b for b in self.model.books if b.is_overdue()]
        if overdue:
            QtWidgets.QMessageBox.warning(self, "Uwaga", f"Masz {len(overdue)} przeterminowanych książek!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

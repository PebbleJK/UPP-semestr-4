import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QStatusBar, QDialog, QDialogButtonBox, QVBoxLayout, QMessageBox
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import QSize, Qt

# QDialog - Zadanie 3
class CloseDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle(":c")

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Close the application?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Learning App")
    centralWidget = QWidget()
    self.setCentralWidget(centralWidget)

    # Dodawanie menu - Zadanie 1
    # OBRAZKI ZNAJDUJĄ SIĘ W GŁÓWNYM FOLDERZE "PROGRAMOWANIE OBIEKTOWE"
    menubar = self.menuBar()
    mathMenu = menubar.addMenu("&Math")
    addSubMenu = mathMenu.addMenu("+/-")
    mathMenu.addSeparator()
    doubleHalveMenu = mathMenu.addMenu("*/:")

    actionsMenu = menubar.addMenu("&Actions")

    addOneAction = QAction(QIcon("add.png"), "+1", self)
    addOneAction.setShortcut(QKeySequence("Ctrl+A"))
    addOneAction.setStatusTip("Add 1")
    addOneAction.triggered.connect(self.addOne)

    subOneAction = QAction(QIcon("sub.png"), "-1", self)
    subOneAction.setShortcut(QKeySequence("Ctrl+S"))
    subOneAction.setStatusTip("Subtract 1")
    subOneAction.triggered.connect(self.subtractOne)

    multiplyAction = QAction(QIcon("multiply.png"), "x2", self)
    multiplyAction.setShortcut(QKeySequence("Ctrl+D"))
    multiplyAction.setStatusTip("Multiply by 2")
    multiplyAction.triggered.connect(self.doubleResult)

    halveAction = QAction(QIcon("halve.png"), "/2", self)
    halveAction.setShortcut(QKeySequence("Ctrl+H"))
    halveAction.setStatusTip("Divide by 2")
    halveAction.triggered.connect(self.halveResult)

    resetAction = QAction(QIcon("reset.png"), "&Reset", self)
    resetAction.setShortcut(QKeySequence("Ctrl+R"))
    resetAction.setStatusTip("Reset the result")
    resetAction.triggered.connect(self.resetResult)

    closeAction = QAction(QIcon("close.png"), "&Close", self)
    closeAction.setShortcut(QKeySequence("Ctrl+Q"))
    closeAction.setStatusTip("Close the application")
    closeAction.triggered.connect(self.closeWindow)

    addSubMenu.addAction(addOneAction)
    addSubMenu.addSeparator()
    addSubMenu.addAction(subOneAction)

    doubleHalveMenu.addAction(multiplyAction)
    doubleHalveMenu.addSeparator()
    doubleHalveMenu.addAction(halveAction)

    actionsMenu.addAction(resetAction)
    actionsMenu.addSeparator()
    actionsMenu.addAction(closeAction)

    # Tworzenie toolbara - Zadanie 2
    toolbar = self.addToolBar("Math Toolbar")
    toolbar.setOrientation(Qt.Vertical)
    toolbar.setStyleSheet("border-right: 1px solid black; padding: 4px;")
    toolbar.setIconSize(QSize(16,16))
    toolbar.addAction(addOneAction)
    toolbar.addSeparator()
    toolbar.addAction(subOneAction)
    toolbar.addSeparator()
    toolbar.addAction(multiplyAction)
    toolbar.addSeparator()
    toolbar.addAction(halveAction)
    toolbar.addSeparator()
    toolbar.addAction(resetAction)
    toolbar.addSeparator()
    toolbar.addAction(closeAction)

    statusBar = QStatusBar(self)
    statusBar.setStyleSheet("background-color: lightgray;")
    self.setStatusBar(statusBar)

    self.wynik = 0
    self.wynikLabel = QLabel(f"Wynik: {self.wynik}")


    layout = QGridLayout()
    layout.setContentsMargins(0, 10, 10, 10)
    layout.addWidget(toolbar, 0, 0, 3, 1)
    layout.addWidget(self.wynikLabel, 1, 2)

    addButton = QPushButton("+1")
    addButton.clicked.connect(self.addOne)
    layout.addWidget(addButton, 0, 1)

    substractButton = QPushButton("-1")
    substractButton.clicked.connect(self.subtractOne)
    layout.addWidget(substractButton, 0, 3)

    multiplyButton = QPushButton("x2")
    multiplyButton.clicked.connect(self.doubleResult)
    layout.addWidget(multiplyButton, 2, 1)

    divideButton = QPushButton("/2")
    divideButton.clicked.connect(self.halveResult)
    layout.addWidget(divideButton, 2, 3)

    centralWidget.setLayout(layout)

  def addOne(self):
    self.wynik += 1
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def subtractOne(self):
    self.wynik -= 1
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def doubleResult(self):
    self.wynik *= 2
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def halveResult(self):
    self.wynik /= 2
    self.wynikLabel.setText(f"Wynik: {self.wynik}")

  def resetResult(self):
    # QMessageBox - Zadanie 3
    dlg = QMessageBox(self)
    dlg.setWindowTitle("Reset")
    dlg.setText("Do you want to reset the result?")
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setIcon(QMessageBox.Question)
    if dlg.exec() == QMessageBox.Yes:
      self.wynik = 0
      self.wynikLabel.setText(f"Wynik: {self.wynik}")    

  def closeWindow(self):
    dlg = CloseDialog(self)
    if dlg.exec():
      self.close()

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())


if __name__ == "__main__":
  main()


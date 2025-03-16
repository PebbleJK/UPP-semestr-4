import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QVBoxLayout, QRadioButton, QCheckBox, QPushButton, QScrollArea, QButtonGroup, QMessageBox, QLineEdit
from PySide6.QtCore import Qt

def stylizuj_tekst(tekst):
    return f"<div style='background-color:white; color:black; padding:5px;'><b>{tekst}</b></div>"

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marvel Quiz")
        # Zmienna na imie
        # Tak jak mówiłeś na zajęciach zamiast zrobić input na odpowiedź i przyrównywać tekst, po prostu pobieram imię osoby
        self.imie = ""
        # Zmienne na style dobrych i złych odpowiedzi
        self.dobraOdpowiedz = "background-color: green;"
        self.zlaOdpowiedz = "background-color: red;"

        scroll_area = QScrollArea()
        centralny_widget = QWidget()

        scroll_area.setWidget(centralny_widget)
        scroll_area.setWidgetResizable(True)
        # Scrollbar po lewej da się ustawić odwracając orientację okienka ale to sprawia że wszystko jest odwrócone
        # w tym kodzie. Chyba trzebaby ułożyć inaczej elementy żeby nie były zależne od scrollbara
        # Albo najlepiej tak nie robić :)
        scroll_area.setLayoutDirection(Qt.RightToLeft)
        # Trzeba ponownie odw
        #scroll_area.verticalScrollBar().setInvertedAppearance(True)
        # Wyłączenie poziomego scrollbara
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setCentralWidget(scroll_area)
        # Zmiana wymiarów okna
        self.resize(1000,350)

        layout = QVBoxLayout()

        self.tytul = QLabel("MARVEL QUIZ - PYTANIA Z MCU")
        self.tytul.setAlignment(Qt.AlignCenter)
        self.tytul.setStyleSheet("font-weight: bold")
        layout.addWidget(self.tytul)

        # Pytanie nr 1:
        self.pytanie1 = QLabel(stylizuj_tekst("1. Kto jest Iron Manem:"))
        self.radio_group1 = QButtonGroup(self)
        self.radio_button1_1 = QRadioButton("Tony Stark")
        self.radio_button1_2 = QRadioButton("Steve Rogers")
        self.radio_button1_3 = QRadioButton("Bruce Banner")

        self.radio_group1.addButton(self.radio_button1_1)
        self.radio_group1.addButton(self.radio_button1_2)
        self.radio_group1.addButton(self.radio_button1_3)

        layout.addWidget(self.pytanie1)
        layout.addWidget(self.radio_button1_1)
        layout.addWidget(self.radio_button1_2)
        layout.addWidget(self.radio_button1_3)

        # Pytanie nr 2:
        self.pytanie2 = QLabel(stylizuj_tekst("2. Kto z poniższych jest członkiem Avengers:"))
        self.checkbox2_1 = QCheckBox("Thor")
        self.checkbox2_2 = QCheckBox("Loki")
        self.checkbox2_3 = QCheckBox("Hawkeye")

        layout.addWidget(self.pytanie2)
        layout.addWidget(self.checkbox2_1)
        layout.addWidget(self.checkbox2_2)
        layout.addWidget(self.checkbox2_3)

        # Pytanie nr 3:
        self.pytanie3 = QLabel(stylizuj_tekst("3. Kto gra rolę Thora w filmach Marvela?"))
        self.radio_group3 = QButtonGroup(self)
        self.radio_button3_1 = QRadioButton("Chris Hemsworth")
        self.radio_button3_2 = QRadioButton("Chris Evans")
        self.radio_button3_3 = QRadioButton("Chris Pratt")

        self.radio_group3.addButton(self.radio_button3_1)
        self.radio_group3.addButton(self.radio_button3_2)
        self.radio_group3.addButton(self.radio_button3_3)

        layout.addWidget(self.pytanie3)
        layout.addWidget(self.radio_button3_1)
        layout.addWidget(self.radio_button3_2)
        layout.addWidget(self.radio_button3_3)

        # Pytanie nr 4:
        self.pytanie4 = QLabel(stylizuj_tekst("4. Kto jest siostrą Gamory:"))
        self.radio_group4 = QButtonGroup(self)
        self.radio_button4_1 = QRadioButton("Nebula")
        self.radio_button4_2 = QRadioButton("Valkyrie")
        self.radio_button4_3 = QRadioButton("Shuri")

        self.radio_group4.addButton(self.radio_button4_1)
        self.radio_group4.addButton(self.radio_button4_2)
        self.radio_group4.addButton(self.radio_button4_3)

        layout.addWidget(self.pytanie4)
        layout.addWidget(self.radio_button4_1)
        layout.addWidget(self.radio_button4_2)
        layout.addWidget(self.radio_button4_3)

        # Pytanie nr 5:
        self.pytanie5 = QLabel(stylizuj_tekst("Które z poniższych postaci występuje w filmie 'Guardians of the Galaxy':"))
        self.checkbox5_1 = QCheckBox("Rocket Racoon")
        self.checkbox5_2 = QCheckBox("Black Widow")
        self.checkbox5_3 = QCheckBox("Drax the Destroyer")

        layout.addWidget(self.pytanie5)
        layout.addWidget(self.checkbox5_1)
        layout.addWidget(self.checkbox5_2)
        layout.addWidget(self.checkbox5_3)

        centralny_widget.setLayout(layout)

        # Dodanie inputa na imie
        self.inputImie = QLineEdit()
        self.inputImie.setPlaceholderText("Podaj imie")
        layout.addWidget(self.inputImie)

        # Przycisk sprawdzający:

        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        layout.addWidget(self.check_button)

    def sprawdzenie_odp(self):
        punkty = 0

        if self.radio_button1_1.isChecked():
            punkty += 1
        
        if self.checkbox2_1.isChecked() and not self.checkbox2_2.isChecked() and self.checkbox2_3.isChecked():
            punkty += 1
        
        if self.radio_button3_1.isChecked():
            punkty += 1
        
        if self.radio_button4_1.isChecked():
            punkty += 1
        
        if self.checkbox5_1.isChecked() and not self.checkbox5_2.isChecked() and self.checkbox5_3.isChecked():
            punkty += 1
        
        # Pobranie imienia
        self.imie = self.inputImie.text()

        # Dodanie imienia do wiadomości na końcu
        QMessageBox.information(self, "Wynik", f"{self.imie}, zdobyłeś/aś {punkty} na 5 punktów!")

        # Zaznaczenie pobrawnych i niepoprawnych odpowiedzi

        # Poprawne
        self.radio_button1_1.setStyleSheet(self.dobraOdpowiedz)
        self.checkbox2_1.setStyleSheet(self.dobraOdpowiedz)
        self.checkbox2_3.setStyleSheet(self.dobraOdpowiedz)
        self.radio_button3_1.setStyleSheet(self.dobraOdpowiedz)
        self.radio_button4_1.setStyleSheet(self.dobraOdpowiedz)
        self.checkbox5_1.setStyleSheet(self.dobraOdpowiedz)
        self.checkbox5_3.setStyleSheet(self.dobraOdpowiedz)
        # Niepoprawne
        # Niepoprawnych nie piszę bo za dużo kopiuj wklej, a to to samo co z poprawnymi


app = QApplication([])
quiz = Quiz()
quiz.show()
app.exec()





    


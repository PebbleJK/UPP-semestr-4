import mysql.connector
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QGroupBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MySQL Database Connect")
        self.setGeometry(100, 100, 500, 100)

        # Labels
        name_label = QLabel("Name")
        profession_label = QLabel("Proffesion")
        address_label = QLabel("Address")
        age_label = QLabel("Age")

        # Line edits
        self.name_line_edit = QLineEdit()
        self.profession_line_edit = QLineEdit()
        self.address_line_edit = QLineEdit()
        self.age_line_edit = QLineEdit()

        # Buttons
        button_add_data = QPushButton("Add new row")
        button_add_data.clicked.connect(self.add_data)

        button_update_data = QPushButton("Update selected row")
        button_update_data.clicked.connect(self.update_data)



        # Name layout
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name_label)
        h_layout1.addWidget(self.name_line_edit)

        # Proffesion layout
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(profession_label)
        h_layout2.addWidget(self.profession_line_edit)

        # Address layout
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(address_label)
        h_layout3.addWidget(self.address_line_edit)

        # Age layout
        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(age_label)
        h_layout4.addWidget(self.age_line_edit)

        # Button layout
        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(button_add_data)
        h_layout5.addWidget(button_update_data)

        # Grupowanie label i line edit
        add_form = QGroupBox("Add New Employee")

        # Layout w grupie
        form_layout = QVBoxLayout()
        form_layout.addLayout(h_layout1)
        form_layout.addLayout(h_layout2)
        form_layout.addLayout(h_layout3)
        form_layout.addLayout(h_layout4)
        form_layout.addLayout(h_layout5)
        add_form.setLayout(form_layout)

        # Table
        self.table = QTableWidget(self)
        self.table.setMaximumWidth(800)

        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 50)

        self.table.setHorizontalHeaderLabels(["Name", "Proffesion", "Address", "Age"])

        # Buttony pod table
        button_insert_data = QPushButton("Insert demo content")
        button_insert_data.clicked.connect(self.insert_data)

        button_load_data = QPushButton("Load data")
        button_load_data.clicked.connect(self.load_data)

        button_call_data = QPushButton("Extract data")
        button_call_data.clicked.connect(self.call_data)

        button_delete_data = QPushButton("Delete data")
        button_delete_data.clicked.connect(self.delete_data)

        # Wyświetlanie
        layout = QVBoxLayout()
        layout.addWidget(add_form)
        layout.addWidget(self.table)
        layout.addWidget(button_insert_data)
        layout.addWidget(button_load_data)
        layout.addWidget(button_call_data)
        layout.addWidget(button_delete_data)
        self.setLayout(layout)


    def create_connection(self):
        # Połączenie z bazą mysql
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "employees"
        )
        return self.mydb
    
    def insert_data(self):
        # Obiekt pozwalający na wykonywanie zapytań
        cursor = self.create_connection().cursor()

        # Przykładowe dane
        self.list_of_employes = [
            ("Jakub Kałuża", "Praktykant", "Poznań 1", 24),
            ("Pracownik1", "Zawód1", "Adres1", 31),
            ("Pracownik2", "Zawód2", "Adres2", 32),
            ("Pracownik3", "Zawód3", "Adres3", 33)
        ]

        # Wstawianie kilku wierszy
        cursor.executemany("insert into employees_list (Name, Profession, Address, Age) values (%s, %s, %s, %s)", self.list_of_employes)
        print("Demo data inserted in table")
        # Zapisanie zmian w ramach bieżącego połączenia
        self.mydb.commit()
        # Zamknięcie połączenia
        self.mydb.close()
    
    def load_data(self):
        cursor = self.create_connection().cursor()

        sqlquery = "SELECT * FROM employees_list"

        # Ustawia ilość wierszy w tabeli na taką jaką zwróci zapytanie
        self.table.setRowCount(len(sqlquery))

        # Dodawanie każdego pracownika z bazy do tabeli
        table_row = 0

        # Pobranie wszystkich wierszy z bazy
        cursor.execute(sqlquery)
        records = cursor.fetchall()

        # Ustawia ilość wierszy w tabeli na taką jaką zwróci zapytanie
        self.table.setRowCount(len(records))

        # Wyświetlenie pobranych danych
        for i in records:
            self.table.setItem(table_row, 0, QTableWidgetItem(i[0]))
            self.table.setItem(table_row, 1, QTableWidgetItem(i[1]))
            self.table.setItem(table_row, 2, QTableWidgetItem(i[2]))
            self.table.setItem(table_row, 3, QTableWidgetItem(str(i[3])))
            table_row = table_row + 1

        self.mydb.commit()
        self.mydb.close()
    
    def add_data(self):
        cursor = self.create_connection().cursor()

        # Pobranie danych z inputów do listy
        self.new_employee = [
            self.name_line_edit.text(),
            self.profession_line_edit.text(),
            self.address_line_edit.text(),
            self.age_line_edit.text(),
        ]

        # Dodanie wiersza do bazy
        cursor.execute("INSERT into employees_list (Name, Profession, Address, Age) values (%s, %s, %s, %s)", self.new_employee)
        print("Dodano wiersz do bazy")

        # Czyszczenie inputów
        self.name_line_edit.clear()
        self.profession_line_edit.clear()
        self.address_line_edit.clear()
        self.age_line_edit.clear()
        
        self.mydb.commit()
        self.mydb.close()
    
    def call_data(self):
        # Przepisanie wybranego wiersza do inputów
        current_row_index = self.table.currentRow()
        self.name_edit = str(self.table.item(current_row_index, 0).text())
        self.profession_edit = str(self.table.item(current_row_index, 1).text())
        self.address_edit = str(self.table.item(current_row_index, 2).text())
        self.age_edit = str(self.table.item(current_row_index, 3).text())

        self.name_line_edit.setText(self.name_edit)
        self.profession_line_edit.setText(self.profession_edit)
        self.address_line_edit.setText(self.address_edit)
        self.age_line_edit.setText(self.age_edit)
    
    def update_data(self):
        cursor = self.create_connection().cursor()

        # Pobranie danych z inputów do listy
        new_values = (
            self.name_line_edit.text(),
            self.profession_line_edit.text(),
            self.address_line_edit.text(),
            self.age_line_edit.text(),
            self.name_edit
        )

        # Zmiana danych
        cursor.execute("UPDATE employees_list SET Name=%s, Profession=%s, Address=%s, Age=%s WHERE name=%s", new_values)
        print("Zaktualizowano wiersz")

        # Wyczyszczenie inputów
        self.name_line_edit.clear()
        self.profession_line_edit.clear()
        self.address_line_edit.clear()
        self.age_line_edit.clear()

        self.mydb.commit()
        self.mydb.close()
    
    def delete_data(self):
        cursor = self.create_connection().cursor()
        current_row_index = self.table.currentRow()
        
        if current_row_index < 0:
            warning = QMessageBox.warning(self, "Warning", "Please select a record to delete")
        else:
            name_item = str(self.table.item(current_row_index, 0).text())
            cursor.execute("DELETE FROM employees_list WHERE Name=%s", [name_item])
        
        self.mydb.commit()
        self.mydb.close()

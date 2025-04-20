import os

class CommandHistory:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, command):
        print(f"Wykonano: {command}")
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Brak poleceń do cofnięcia.")
            return
        command = self.undo_stack.pop()
        self.redo_stack.append(command)
        print(f"Cofnięto: {command}")

    def redo(self):
        if not self.redo_stack:
            print("Brak poleceń do ponownego wykonania.")
            return
        command = self.redo_stack.pop()
        self.undo_stack.append(command)
        print(f"Ponownie wykonano: {command}")

    def delete(self, command):
        if command in self.undo_stack:
            self.undo_stack.remove(command)
            print(f"Usunięto z historii: {command}")
        elif command in self.redo_stack:
            self.redo_stack.remove(command)
            print(f"Usunięto z kolejki REDO: {command}")
        else:
            print(f"Nie znaleziono polecenia: {command}")

    def show_history(self):
        print("Historia (UNDO):", self.undo_stack)
        print("Historia (REDO):", self.redo_stack)

def menu():
    h = CommandHistory()
    while True:
        os.system('cls')
        print("=== MENU ===")
        print("1. Wykonaj polecenie")
        print("2. Cofnij (UNDO)")
        print("3. Ponów (REDO)")
        print("4. Usuń polecenie")
        print("5. Pokaż historię")
        print("6. Wyjdź")
        choice = input("Wybierz opcję: ")

        os.system('cls')
        if choice == "1":
            command = input("Podaj polecenie do wykonania: ")
            h.execute(command)
        elif choice == "2":
            h.undo()
        elif choice == "3":
            h.redo()
        elif choice == "4":
            command = input("Podaj polecenie do usunięcia: ")
            h.delete(command)
        elif choice == "5":
            h.show_history()
        elif choice == "6":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        input("\nNaciśnij Enter, aby kontynuować...")


menu()
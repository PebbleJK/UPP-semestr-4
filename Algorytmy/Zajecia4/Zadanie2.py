from collections import deque
from datetime import datetime
import os

class Notification:
    def __init__(self, message, type_, priority='normal'):
        self.message = message
        self.type = type_  # 'info', 'warning', 'error'
        self.timestamp = datetime.now()
        self.priority = priority  # 'normal' or 'urgent'

    def __repr__(self):
        return f"[{self.timestamp.strftime('%H:%M:%S')}][{self.priority.upper()}][{self.type.upper()}] {self.message}"


class NotificationSystem:
    def __init__(self, normal_limit=5):
        self.queue = deque()
        self.normal_limit = normal_limit

    def add_notification(self, message, type_, priority='normal'):
        notification = Notification(message, type_, priority)

        if priority == 'urgent':
            self.queue.appendleft(notification)
        else:
            normal_count = sum(1 for n in self.queue if n.priority == 'normal')
            if normal_count >= self.normal_limit:
                for i in range(len(self.queue)):
                    if self.queue[i].priority == 'normal':
                        removed = self.queue[i]
                        del self.queue[i]
                        print(f"Usunięto stare powiadomienie: {removed}")
                        break
            self.queue.append(notification)

        print(f"Dodano powiadomienie: {notification}")

    def get_next_notification(self):
        if not self.queue:
            print("Brak powiadomień.")
            return None
        notif = self.queue.popleft()
        print(f"Wyświetlono: {notif}")
        return notif

    def pending_count(self):
        return len(self.queue)

    def show_all(self):
        if not self.queue:
            print("\nBrak oczekujących powiadomień.\n")
        else:
            print("\nOczekujące powiadomienia:")
            for n in self.queue:
                print(n)
            print("")
            print(f"Liczba: {len(self.queue)}\n")


def show_menu():
    print("\n=== SYSTEM POWIADOMIEŃ ===")
    print("1. Dodaj powiadomienie")
    print("2. Wyświetl następne powiadomienie")
    print("3. Pokaż wszystkie oczekujące")
    print("4. Pokaż liczbę oczekujących")
    print("5. Wyjście")


def main():
    system = NotificationSystem(normal_limit=3)

    while True:
        os.system('cls')
        show_menu()
        choice = input("Wybierz opcję (1-5): ")

        if choice == '1':
            os.system('cls')
            msg = input("Treść powiadomienia: ")
            type_ = input("Typ (info/warning/error): ").lower()
            priority = input("Priorytet (normal/urgent): ").lower()
            system.add_notification(msg, type_, priority)
            input("\nNaciśnij Enter, aby kontynuować...")

        elif choice == '2':
            os.system('cls')
            system.get_next_notification()
            input("\nNaciśnij Enter, aby kontynuować...")

        elif choice == '3':
            os.system('cls')
            system.show_all()
            input("Naciśnij Enter, aby kontynuować...")

        elif choice == '4':
            os.system('cls')
            print(f"Liczba oczekujących powiadomień: {system.pending_count()}")
            input("\nNaciśnij Enter, aby kontynuować...")

        elif choice == '5':
            os.system('cls')
            print("Do widzenia!")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            input("\nNaciśnij Enter, aby kontynuować...")

main()

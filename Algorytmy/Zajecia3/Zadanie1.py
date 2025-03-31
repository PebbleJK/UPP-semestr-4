# Zaimplementuj wyszukiwanie najmniejszego i największego elementu w: tablicy posortowanej, 
# tablicy nieposortowanej oraz BST -  dodaj licznik kroków, określ złożoność czasową i pamięciową.

import random
numbers = [random.randint(1, 1000) for _ in range(100)]
# .copy ponieważ bez tego sort modyfikuje też oryginalną tablicę
sortedNumbers = numbers.copy()
sortedNumbers.sort()

print("[Tablica nieposortowana]")
print(numbers)
print()
print("[Tablica posortowana]")
print(sortedNumbers)
print()

# Najmniejszy i największy element w tablicy posortowanej
# Złożoność O(1)
# Zawsze 2 kroki (lub 3 jak liczymy sprawdzenie długości tablicy)
print("[Tablica posortowana]")
print(f"Najmniejszy element: {sortedNumbers[0]}")
print(f"Największy element: {sortedNumbers[len(sortedNumbers) - 1]}")

print()

# Złożoność O(n)
print("[Tablica nieposortowana]")
def find_min_max(arr):
    if len(arr) == 0:
        return None, None
    min_val = arr[0]
    max_val = arr[0]
    steps = 0
    for num in arr:
        steps += 1
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print(f"Liczba kroków: {steps}")
    return min_val, max_val
numbersMinMax = find_min_max(numbers)
print(f"Najmniejszy element: {numbersMinMax[0]}")
print(f"Największy element: {numbersMinMax[1]}")

print()


# Najmniejszy i największy element w BST
# Złożoność O(h) - h to wysokość drzewa
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Wstawia nową wartość do drzewa BST."""
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def find_min(self):
        current = self
        steps = 0
        while current.left is not None:
            current = current.left
            steps += 1
        print(f"Liczba kroków (find_min): {steps}")
        return current.value

    def find_max(self):
        current = self
        steps = 0
        while current.right is not None:
            current = current.right
            steps += 1
        print(f"Liczba kroków (find_max): {steps}")
        return current.value
    
BSTNumbers = BSTNode(numbers[0])
for num in numbers[1:]:
    BSTNumbers.insert(num)
print("[BST]")
print(f"Najmniejszy element: {BSTNumbers.find_min()}")
print(f"Największy element: {BSTNumbers.find_max()}")

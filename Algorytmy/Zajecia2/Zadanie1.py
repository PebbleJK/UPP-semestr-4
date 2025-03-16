import random
# Dane testowe
test100 = [random.randint(1,100) for i in range(100)]
test10000 = [random.randint(1,100) for i in range(10000)]
test1000000 = [random.randint(1,100) for i in range(1000000)]
# O(1)
# Wypisanie długości tablicy
# Zawsze 1 krok niezależnie od ilości danych
def arrayLength(arr):
  return len(arr)
print(arrayLength(test100))
#print(arrayLength(test10000))
#print(arrayLength(test1000000))
print()

# O(n)
# Wypisanie wszystkich elementów tablicy o długości n
# Licznik kroków nie jest potrzebny
# Zawsze będzie n kroków (n przejść przez pętle)
def printArray(arr):
  for x in arr:
    print(x)
printArray(test100)
#printArray(test10000)
#printArray(test1000000)
print()

# O(n^2)
# Sortowanie bąbelkowe
def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        steps += 1
        for j in range(1, n - i):
            steps += 1
            if arr[j - 1] > arr[j]: 
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(f"Liczba kroków: {steps}")
    return 0
bubble_sort(test100)
print(test100)
#bubble_sort(test10000)
#print(test10000)
#bubble_sort(test1000000)
#print(test1000000)
print()


# O(a^n)
# Rekurencyjny ciąg fibbonacciego
fibbCounter = 0
def fibb(n):
   num1 = 1
   num2 = 1
   global fibbCounter
   if(n < 3):
      fibbCounter += 1
      return 1
   else:
      fibbCounter += 1
      return fibb(n-1) + fibb(n-2)
# Tu nie radzę za dużo wpisywać bo już dla 100 mi wybucha
print(fibb(20))
print(f"Liczba kroków fibb: {fibbCounter}")
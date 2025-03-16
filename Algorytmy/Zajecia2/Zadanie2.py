# a
# Złożoność pamięciowa O(n) - zależne od długości tablicy
# Złożoność czasowa O(n) - dwie niezależne pętle
negativeArr = [1,2,-3,4,-2,-1,2,6,4,-6]
def moveNegativeNumbers(arr):
  newArr = []
  for x in arr:
    if x < 0:
      newArr.append(x)
  for x in arr:
    if x >= 0:
      newArr.append(x)
  return newArr
print(moveNegativeNumbers(negativeArr))
print()

# b
# Złożoność pamięciowa O(n) - zależne od długości tablicy
# Złożoność pamięciowa O(n) - dwie niezależne pętle
missingNumberArr = [1,2,3,4,5,6,7,9]
def findMissingNumber(arr):
  n = len(arr) + 1
  bigFactorial = 1
  smallFactorial = 1
  # Liczę n!
  x = 1
  while(x <= n):
    bigFactorial *= x
    x += 1
  # Mnoże przez siebie wszystkie elementy tablicy (czyli jakby robię silnię bez brakującego elementu)
  for y in arr:
    smallFactorial *= y
  # Brakująca liczba to będzie wynik dzielenia przez siebie obliczonych iloczynów
  return bigFactorial/smallFactorial
print(findMissingNumber(missingNumberArr))
print()

# c
# Złożoność pamięciowa O(n) - zależne od długości tablicy
# Złożoność czasowa O(n) - jedna pętla
arrWithCopies = [1,2,3,4,1,2,5,5,6,7,8,2,554,22,11,44,22,1,4]
def findCopies(arr):
  # set przechowuje unikalne elementy i w nim sprawdzam czy coś już się pojawiło
  seen = set()
  copies = set()
  for x in arr:
    if x in seen:
      copies.add(x)
    seen.add(x)
  return copies
print(f"Duplikaty w tablicy: {findCopies(arrWithCopies)}")
print()


# d
# Myślę że ten algorytm ma złożoność czasową O(n). Co 2 nowe nowe dodane liczby ilość kroków wzrasta stale o 5.
# Złożoność pamięciową również oceniam na O(n) - zależne od długości tablicy
arrToRev = [1, 2, 3, 4, 5, 6, 7, 8]
revCounter = 0
def reverseArr(arr):
  start = 0
  end = len(arr) - 1
  global revCounter
  revCounter += 2
  while(start <= end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
    revCounter += 5
reverseArr(arrToRev)
print(arrToRev)
print(f"Liczba kroków: {revCounter}")

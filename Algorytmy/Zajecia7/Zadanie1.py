# permutacje
def permutacje(lista):
  
  if len(lista) <= 1:
    return [lista[:]] # to podobno zwraca kopię listy a nie referencję
  
  wynik = []
  for i in range(len(lista)):
      x = lista[i]

      listaBezX = lista[:i] + lista[i+1:] #usuwanie użytego znaku

      #permutowanie pozostałych elementów
      for p in permutacje(listaBezX):
          wynik.append([x] + p) #doklejanie permutacji pozostałych elementów

  return wynik

print(permutacje(["J","a","k"]))
print()

# zapis binarny (czytać od dołu)
def binarny(n):
  if n == 1:
    print(1)
  else:
    if n % 2 == 0:
      print(0)
      binarny(n/2)
    else:
      print(1)
      binarny((n-1)/2)

binarny(8)
print()

# labirynt
def labiryntSciezka(labirynt, start, koniec, odwiedzone = None, sciezka = None):
  if odwiedzone is None:
    odwiedzone = set()
  if sciezka is None:
    sciezka = []

  x, y = start

  # Sprawdzenie czy bylo odwiedzone oraz kolizji
  if (x < 0 or x >= len(labirynt) or
        y < 0 or y >= len(labirynt[0]) or
        labirynt[x][y] == 1 or
        (x, y) in odwiedzone):
        return None
  
  sciezka.append((x,y)) # dodanie do sciezki
  odwiedzone.add((x,y)) # oznaczenie ze odwiedzone

  # Znalazł
  if (x, y) == koniec:
        return sciezka

  # Ruchy: dół, góra, prawo, lewo
  kierunki = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for dx, dy in kierunki:
      nowy_x, nowy_y = x + dx, y + dy
      wynik = labiryntSciezka(labirynt, (nowy_x, nowy_y), koniec, odwiedzone, sciezka)
      if wynik is not None:
          return wynik  # znaleziona ścieżka
      
  # Jeśli utknie gdzieś to się cofa
  sciezka.pop()
  return None

labirynt = [ [0, 1, 0, 0],
    	       [0, 0, 0, 1],
   	         [1, 1, 0, 0],
 	           [0, 0, 0, 0] ]
start = (0, 0)
koniec = (3, 3)
print(labiryntSciezka(labirynt, start, koniec))  
  

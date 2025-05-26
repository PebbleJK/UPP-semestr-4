obraz = [[123, 42, 243],
         [  1,  2,  3 ],
         [200, 180, 47]]

# zwykły blur
def blur(obraz):
    wiersze = len(obraz)
    kolumny = len(obraz[0])
    
    wynik = obraz

    for i in range(wiersze):
        for j in range(kolumny):
            suma = 0
            licznik = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < wiersze and 0 <= nj < kolumny:
                        suma += obraz[ni][nj]
                        licznik += 1
            wynik[i][j] = suma / licznik
    return wynik

for wiersz in blur(obraz):
    print(wiersz)
print()

# blur Gaussa
def blurGaussa(obraz):
    wiersze = len(obraz)
    kolumny = len(obraz[0])
    wagi = [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]
    wynik = obraz

    for i in range(wiersze):
        for j in range(kolumny):
            suma = 0
            wagiSuma = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < wiersze and 0 <= nj < kolumny:
                        suma += obraz[ni][nj] * wagi[ni][nj]
                        wagiSuma += wagi[ni][nj]
            wynik[i][j] = suma / wagiSuma
    return wynik

for wiersz in blurGaussa(obraz):
    print(wiersz)
print()

# Zamiana w obraz binarny
def obrazBinarny(obraz, prog):
  for x in range(len(obraz)):
    for y in range(len(obraz[x])):
      if obraz[x][y] < prog:
        obraz[x][y] = 0
      else:
        obraz[x][y] = 1
  return obraz

for wiersz in obrazBinarny(obraz, 100):
    print(wiersz)
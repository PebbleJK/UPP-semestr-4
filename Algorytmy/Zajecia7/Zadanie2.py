# dfs
def flood_fill_dfs(obraz, x, y, nowy_kolor):
    # zapamiętanie szukanego koloru
    stary_kolor = obraz[x][y]
    if stary_kolor == nowy_kolor:
        return

    def dfs(i, j):
        # Sprawdzenie granicy i koloru
        if (i < 0 or i >= len(obraz) or
            j < 0 or j >= len(obraz[0]) or
            obraz[i][j] != stary_kolor):
            return

        obraz[i][j] = nowy_kolor

        # Ruchy: dół, góra, prawo, lewo
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    dfs(x, y)

from collections import deque

def flood_fill_bfs(obraz, x, y, nowy_kolor):
    # Zapamiętanie starego koloru
    stary_kolor = obraz[x][y]
    if stary_kolor == nowy_kolor:
        return

    kolejka = deque()
    kolejka.append((x, y))

    while kolejka:
        i, j = kolejka.popleft()

        # Sprawdzanie granic i koloru
        if (i < 0 or i >= len(obraz) or
            j < 0 or j >= len(obraz[0]) or
            obraz[i][j] != stary_kolor):
            continue

        obraz[i][j] = nowy_kolor

        # Przejście na sąsiadów (dodanie ich do kolejki)
        kolejka.append((i + 1, j))
        kolejka.append((i - 1, j))
        kolejka.append((i, j + 1))
        kolejka.append((i, j - 1))

obraz = [
    [1, 1, 1, 2],
    [1, 1, 0, 2],
    [1, 0, 1, 2]
]

#flood_fill_dfs(obraz, 0, 0, 9)
flood_fill_bfs(obraz, 0, 3, 9)

for wiersz in obraz:
    print(wiersz)
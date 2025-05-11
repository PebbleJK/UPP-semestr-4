from datetime import datetime, timedelta
import random
from collections import defaultdict

# Hashmapa: lokalizacja -> lista dat odwiedzin
odwiedziny = defaultdict(list)

# Funkcja do zapisywania odwiedzin
def zapisz_odwiedziny(lokacje_dict, lokalizacja, czas=None):
    if czas is None:
        czas = datetime.now()
    lokacje_dict[lokalizacja].append(czas)

# 10 lokalizacji
lokalizacje = [
    (52.23, 21.01), (50.06, 19.94), (51.11, 17.03), (53.13, 23.15), (54.35, 18.65),
    (49.82, 19.05), (51.77, 19.46), (52.40, 16.92), (53.43, 14.55), (50.87, 20.63)
]

# Generujemy 30 wpisów – co kilka godzin/dni
czas_bazowy = datetime(2024, 5, 11, 8, 0)
for i in range(30):
    lokalizacja = random.choice(lokalizacje)
    czas = czas_bazowy + timedelta(hours=8 * i)
    zapisz_odwiedziny(odwiedziny, lokalizacja, czas)

# Funkcja: znajdź lokalizacje odwiedzone danego dnia
def znajdz_lokalizacje_dla_dnia(lokacje_dict, data_szukana):
    wynik = set()
    for lokalizacja, daty in lokacje_dict.items():
        for dt in daty:
            if dt.date() == data_szukana.date():
                wynik.add(lokalizacja)
                break  # wystarczy jedno dopasowanie
    return wynik

# Przykład użycia
data_testowa = datetime(2024, 5, 11)  # np. 3 maja
wynik = znajdz_lokalizacje_dla_dnia(odwiedziny, data_testowa)

print(f"Lokalizacje odwiedzone {data_testowa.date()}:")
for loc in wynik:
    print(f"- {loc}")

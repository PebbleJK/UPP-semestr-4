import random
import re
from collections import defaultdict

sample_words = [
    "programowanie", "komputer", "sieć", "system", "aplikacja", "dane", "serwer", "kod",
    "projekt", "oprogramowanie", "interfejs", "moduł", "logika", "skrypt", "python", "zmienna",
    "argument", "funkcja", "plik", "zapis", "odczyt", "debugowanie", "błąd", "test", "kompilacja",
    "struktura", "kontrola", "algorytm", "graf", "drzewo", "kolejka", "stos", "pętla", "warunek"
]

random_text = " ".join(random.choices(sample_words, k=700))

# Funkcja zliczająca słowa według pierwszej litery
def count_words_by_first_letter(text):
    # Usuwanie interpunkcji i zamiana na małe litery (to od chata)
    cleaned_text = re.sub(r"[^\w\s]", "", text.lower())
    
    words = cleaned_text.split(" ")
    
    # Tworzenie słownika który domyślnie przypisuje 0 dla pozycji których nie było
    letter_counts = defaultdict(int)

    for word in words:
        if word:
            first_letter = word[0]
            letter_counts[first_letter] += 1

    # To też sortowanie od chata: krotki, zasada (wg wartości a nie klucza), od tyłu (malejąco)
    sorted_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts

result = count_words_by_first_letter(random_text)
for key, value in result.items():
    print(f"{key}: {value}")

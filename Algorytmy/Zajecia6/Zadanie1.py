TABLE_SIZE = 30  # rozmiar tablicy haszującej

# Prosta funkcja haszująca
# Suma wartości unicode'ów i modulo
def simple_hash(key):
    keySum = 0
    for c in key:
        keySum += ord(c)
    return keySum % TABLE_SIZE

# Horner
# Mnoży wartość przez jakąś bazę i dodaje wartość unicode'u + modulo
def horner_hash(key, base = 31):
    hash_value = 0
    for c in key:
        hash_value = hash_value * base + ord(c)
    return hash_value % TABLE_SIZE

# DJB2
# Zaczyna od wartości 5381, mnoży przez 33 i dodaje wartość unicode'u + modulo
def djb2_hash(key):
    hash_value = 5381
    for c in key:
        hash_value = hash_value * 33 + ord(c)  # ((hash_value << 5) + hash_value) + ord(c) - można tym przesunięciem bitowym
    return hash_value % TABLE_SIZE

# Przykładowe stringi
keys = [f"test{i}" for i in range(30)]

# wypisanie wyników
def compare_hash_functions():
    simple_table = [0] * TABLE_SIZE
    horner_table = [0] * TABLE_SIZE
    djb2_table   = [0] * TABLE_SIZE

    for key in keys:
        simple_table[simple_hash(key) % TABLE_SIZE] += 1
        horner_table[horner_hash(key) % TABLE_SIZE] += 1
        djb2_table[djb2_hash(key) % TABLE_SIZE]     += 1

    print("Indeks | Prosty | Horner | Hash")
    print("-------------------------------")

    # te dwukropki są dla ładniejszej tabelki (oznaczają że to co jest wypisane musi mieć conajmniej x znaków)
    for i in range(TABLE_SIZE):
        print(f"{i:6} | {simple_table[i]:6} | {horner_table[i]:6} | {djb2_table[i]:4}")

compare_hash_functions()


polishWords = [
    "dom", "szkoła", "komputer", "książka", "samochód", "telefon", "ogród", "miasto", "dziecko", "nauczyciel",
    "pies", "kot", "drzewo", "rzeka", "jezioro", "góry", "las", "chleb", "mleko", "ser", "jabłko", "banan",
    "krzesło", "stół", "okno", "drzwi", "łóżko", "szafa", "rower", "zegar", "kwiat", "słońce", "księżyc",
    "gwiazda", "niebo", "deszcz", "śnieg", "wiatr", "burza", "morze", "plaża", "piasek", "fala", "ryba",
    "ptak", "samolot", "pociąg", "autobus", "droga", "most", "ulica", "sklep", "kino", "teatr", "muzeum",
    "biblioteka", "park", "zoo", "szpital", "apteka", "restauracja", "hotel", "bank", "pieniądze", "karta",
    "klucz", "torba", "walizka", "buty", "ubranie", "czapka", "rękawiczki", "szalik", "kurtka", "spodnie",
    "koszula", "bluza", "sukienka", "spódnica", "zegarek", "pierścionek", "naszyjnik", "kolczyki", "bransoletka",
    "plecak", "książeczka", "gazeta", "czasopismo", "telewizor", "radio", "komórka", "laptop", "mysz", "klawiatura",
    "monitor", "drukarka", "skaner", "aparat", "kamera", "mikrofon", "głośnik", "słuchawki", "pilot", "bateria",
    "ładowarka", "kabel", "przycisk", "program", "gra", "film", "muzyka", "piosenka", "taniec", "obraz", "rysunek",
    "malarstwo", "rzeźba", "fotografia", "sport", "piłka", "rower", "narty", "łyżwy", "basen", "siłownia", "bieganie",
    "skakanie", "wspinaczka", "jazda", "samochód", "motocykl", "traktor", "statek", "łódź", "kajak", "żaglówka",
    "rakieta", "kosmos", "planeta", "gwiazdozbiór", "galaktyka", "czarna dziura", "satelita", "teleskop", "astronauta",
    "nauka", "matematyka", "fizyka", "chemia", "biologia", "geografia", "historia", "język", "literatura", "sztuka",
    "filozofia", "psychologia", "socjologia", "ekonomia", "informatyka", "technologia", "medycyna", "prawo", "polityka",
    "religia", "kultura", "tradycja", "święto", "urodziny", "imieniny", "wesela", "pogrzeb", "zwyczaj", "obrzęd",
    "wiara", "modlitwa", "kościół", "cerkiew", "synagoga", "meczet", "świątynia", "klasztor", "kaplica", "ołtarz",
    "jabłonka", "gruszka", "śliwka", "wiśnia", "czereśnia", "brzoskwinia", "morela", "nektarynka", "malina", "truskawka",
    "poziomka", "borówka", "żurawina", "jeżyna", "agrest", "porzeczka", "winogrono", "arbuz", "melon", "dynia",
    "ogórek", "pomidor", "papryka", "marchew", "pietruszka", "seler", "burak", "rzodkiewka", "sałata", "kapusta",
    "kalafior", "brokuł", "szpinak", "jarmuż", "rukola", "koper", "bazylia", "oregano", "tymianek", "rozmaryn",
    "majeranek", "estragon", "czosnek", "cebula", "por", "szczypiorek", "ziemniak", "batat", "cukinia", "bakłażan",
    "fasola", "groch", "soczewica", "ciecierzyca", "ryż", "kasza", "makaron", "chlebek", "bułka", "rogalik",
    "pączek", "ciasto", "tort", "ciastko", "herbatnik", "piernik", "sernik", "szarlotka", "makowiec", "keks",
    "drożdżówka", "chałka", "bagietka", "tost", "naleśnik", "omlet", "jajecznica", "jajko", "kotlet", "schabowy",
    "gulasz", "zupa", "rosół", "barszcz", "żurek", "krupnik", "pomidorowa", "ogórkowa", "grzybowa", "kapuśniak",
    "grochówka", "flaki", "chłodnik", "krem", "sałatka", "surówka", "kanapka", "zapiekanka", "pizza", "hamburger",
    "hotdog", "frytki", "chipsy", "popcorn", "orzeszki", "migdały", "pistacje", "nasiona", "ziarna", "miód",
    "dżem", "konfitura", "syrop", "sok", "kompot", "herbata", "kawa", "kakao", "mleczko", "śmietana",
    "masło", "margaryna", "olej", "oliwa", "ocet", "sól", "pieprz", "cukier", "mąka", "drożdże",
    "proszek", "soda", "wanilia", "cynamon", "goździki", "imbir", "kurkuma", "papryka", "chili", "pieprznik",
    "grzyb", "borowik", "maślak", "koźlarz", "kurka", "pieczarka", "trufla", "smardz", "kania", "sowa",
    "lis", "jeleń", "sarna", "dzik", "zając", "borsuk", "wydra", "bobry", "wiewiórka", "mysz",
    "szczur", "kret", "jeż", "żaba", "ropucha", "traszka", "salamandra", "jaszczurka", "wąż", "żółw",
    "ryś", "wilk", "niedźwiedź", "orzeł", "sokół", "jastrząb", "kruk", "wrona", "sroka", "kawka",
    "wróbel", "jaskółka", "kos", "szpak", "dzięcioł", "sikorka", "czapla", "bocian", "żuraw", "łabędź",
    "kaczka", "gęś", "indyk", "kogut", "kura", "perliczka", "paw", "bażant", "kuropatwa", "czekolada"
]

# złożoność O(n)
# kroków tyle co elementów w tablicy
def wordWithPrefix(arr, prefix):
    for word in arr:
        if word.startswith(prefix):
            print(word)
wordWithPrefix(polishWords, "kot")

print()

# Trie
# Złożoność O(n) wg internetu
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.steps = 0

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def words_with_prefix(self, prefix):
        self.steps = 0
        current = self.root
        for char in prefix:
            self.steps += 1
            if char not in current.children:
                print(f"Liczba kroków (prefix search): {self.steps}")
                return []
            current = current.children[char]
        
        results = []
        self._dfs(current, prefix, results)
        print(f"Liczba kroków (DFS): {self.steps}")
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            self.steps += 1
            self._dfs(child_node, prefix + char, results)

trie = Trie()

for word in polishWords:
    trie.insert(word)

print(trie.words_with_prefix("kot"))
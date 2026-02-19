"""Katalog Filmów / Książek / Gier: "Możecie stworzyć bazę danych filmów, książek czy gier. Dodawanie pozycji, przypisywanie gatunków, ocenianie.'"""

# ścieżki do baz danych
baza_filmow = r"FILMY/baza_filmow.txt"
baza_gier = r"GRYY/baza_gier.txt"
baza_ksiazek = r"KSIAZKI/baza_ksiazek.txt"

# zmienne globalne
global filmy
global gry
global ksiazki

# wczytanie danych jako słownika - tu będzie zmiana na podanie jako argument ścieżki i będzie jedna funkcja do 3 baz
def wczytanie_filmow():
    slownik_filmow = dict()
    with open(baza_filmow, 'r', encoding='utf-8') as file:
        wszystkie_linie = file.readlines()
        lp = 1
        for linia in wszystkie_linie:
            linia = linia.split(";")
            tytul = linia[0].strip()
            rok = linia[1].strip()
            rezyser = linia[2].strip()
            gatunek = linia[3].strip()
            ocena = linia[4].strip()
            opis = linia[5].strip()
            opinia = linia[6].strip()
            slownik_filmow[lp] = {"Tytuł":tytul, "Rok":rok, "Reżyser":rezyser, 3:gatunek, 3:ocena, 5:opis, 6:opinia} # dokonczyc
            lp += 1
    return slownik_filmow
katalog_filmow = wczytanie_filmow()
print(katalog_filmow)
# strip() enterów i spacji

# Funkcje operacyjne katalogów:







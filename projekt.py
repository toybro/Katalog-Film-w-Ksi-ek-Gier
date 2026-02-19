"""Katalog Filmów / Książek / Gier: "Możecie stworzyć bazę danych filmów, książek czy gier. Dodawanie pozycji, przypisywanie gatunków, ocenianie.'"""

# Funkcje operacyjne katalogów:
baza_filmow = r"FILMY/baza_filmow.txt"
baza_gier = r"GRYY/baza_gier.txt"
baza_ksiazek = r"KSIAZKI/baza_ksiazek.txt"

global filmy
global gry
global ksiazki


def wczytanie_filmow():
    with open(baza_filmow) as f:
        wszystkie_linie = f.readlines()
        print(wszystkie_linie)
    return wszystkie_linie
katalog_filmow = wczytanie_filmow()







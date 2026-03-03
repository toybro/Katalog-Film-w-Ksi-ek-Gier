"""Katalog Filmów / Książek / Gier: "Możecie stworzyć bazę danych filmów, książek czy gier.
Dodawanie pozycji, przypisywanie gatunków, ocenianie."""

# import niezbędnych bibliotek:
import os

class MovieDatabase:
    database_exist = None
    films_data_dict = {}
    def __init__(self, filename):    
        self.filename = filename
        # Sprawdzenie, czy katalog istnieje, jeżeli nie, to zostanie utworzony:
        if not os.path.exists("FILMY"):
            os.makedirs("FILMY")
            movie_genre = ["Akcja","Animacja", "Anime", "Baśń", "Biograficzny", "Dokumentalny",
                           "Dramat", "Edukacyjny", "Fmilijny", "Fantasy", "Historyczny", "Horror",
                           "Katastroficzny", "Komedia", "Kryminał", "Melodramat", "Muzyczny", "Przygodowy",
                           "Przyrodniczy", "Psychologiczny", "Romans", "Sci-Fi", "Sensacyjny", "Sportowy",
                           "Thriller", "Wojenny", "Western"]
            # Utworzenie pliku z gatunkami filmowymi:
            with open(r"FILMY/gatunki_filmow.txt", 'w') as file:
                for element in movie_genre:
                    file.writelines(element + "\n")            
        # sprawdzenie, czy baza istnieje, jeżeli nie, to pusta baza zostanie stworzona:
        if not os.path.exists(self.filename):
            MovieDatabase.database_exist = False
            with open(self.filename, 'w') as file:    
                pass
        else:
            MovieDatabase.database_exist = True
    
    # wczytanie danych filmów jako słownika - tu będzie zmiana na podanie jako argument ścieżki i będzie jedna funkcja do 3 baz 
    # albo po użyć if_ów, w zależności od podanej ścieżki!! Ważne!!
    def load_flms_data(self):
        films_data_dict = dict()
        with open(self.filename, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            lp = 1
            for line in all_lines:
                if line == "\n":
                    continue
                else:
                    line = line.split(";")
                    title = line[0].strip()
                    year = line[1].strip()
                    director = line[2].strip()
                    genre = line[3].strip()
                    rating = line[4].strip()
                    description = line[5].strip()
                    opinions = line[6].strip()
                    films_data_dict[lp] = {"Tytuł":title, "Rok":year, "Reżyser":director, "Gatunek":genre, "Ocena":rating, "Opis":description, "Opinie":opinions} # dokonczyc
                    lp += 1
        return films_data_dict

    def remove_movie(self, key):
        # usunięcie filmu po jego numerze i aktualizacja bazy:
        data = []
        lp = 1
        with open(self.filename, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()           
            for line in all_lines:
                if lp == key:
                    lp += 1
                    continue
#                   data.append("\n")

                else:
                    data.append(line)
                lp += 1
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.writelines(data)
    
########################################
    
    def search_movie(self):
        # szukanie filmu w bazie - z Entry
        pass

    def add_movie(self):
        # dodanie filmu do bazy
        pass

    def edit_movie_data(self):
        pass
        
    def add_movie_opinion(self):
        # z Entry
        pass

    def add_movie_rating(self):
        # z Entry - i zaciągnięcie i nadpisanie
        pass    



if __name__ == "__main__":
    print("hello")
    films = MovieDatabase(r"FILMY/baza_filmow.txt")
    print(films.load_flms_data())
    films.remove_movie(1)
    print()
    print(films.load_flms_data())

 



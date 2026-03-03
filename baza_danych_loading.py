"""Warstwa dostępu do danych dla katalogów: filmy, gry i książki."""

import os


class BaseDatabase:
    database_exist = None

    def __init__(self, filename, folder, genres_filename, default_genres=None):
        self.filename = filename
        self.folder = folder
        self.genres_filename = genres_filename
        self.default_genres = default_genres or []

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        genres_path = os.path.join(self.folder, self.genres_filename)
        if not os.path.exists(genres_path) and self.default_genres:
            with open(genres_path, "w", encoding="utf-8") as file:
                for element in self.default_genres:
                    file.write(element + "\n")

        if not os.path.exists(self.filename):
            self.__class__.database_exist = False
            with open(self.filename, "w", encoding="utf-8"):
                pass
        else:
            self.__class__.database_exist = True

    def _load_data(self, creator_key):
        data_dict = {}
        with open(self.filename, "r", encoding="utf-8") as file:
            all_lines = file.readlines()
            lp = 1
            for line in all_lines:
                if line.strip() == "":
                    continue

                parts = line.strip().split(";", 6)
                if len(parts) < 7:
                    parts += [""] * (7 - len(parts))

                title, year, creator, genre, rating, description, opinions = [p.strip() for p in parts]
                data_dict[lp] = {
                    "Tytuł": title,
                    "Rok": year,
                    creator_key: creator,
                    "Gatunek": genre,
                    "Ocena": rating,
                    "Opis": description,
                    "Opinie": opinions,
                }
                lp += 1
        return data_dict

    def remove_entry(self, key):
        data = []
        with open(self.filename, "r", encoding="utf-8") as file:
            all_lines = file.readlines()
            for index, line in enumerate(all_lines, start=1):
                if index != key and line.strip():
                    data.append(line if line.endswith("\n") else line + "\n")

        with open(self.filename, "w", encoding="utf-8") as file:
            file.writelines(data)


class MovieDatabase(BaseDatabase):
    def __init__(self, filename):
        movie_genre = [
            "Akcja", "Animacja", "Anime", "Baśń", "Biograficzny", "Dokumentalny",
            "Dramat", "Edukacyjny", "Familijny", "Fantasy", "Historyczny", "Horror",
            "Katastroficzny", "Komedia", "Kryminał", "Melodramat", "Muzyczny", "Przygodowy",
            "Przyrodniczy", "Psychologiczny", "Romans", "Sci-Fi", "Sensacyjny", "Sportowy",
            "Thriller", "Wojenny", "Western"
        ]
        super().__init__(filename, "FILMY", "gatunki_filmow.txt", movie_genre)

    def load_flms_data(self):
        return self._load_data("Reżyser")

    def remove_movie(self, key):
        self.remove_entry(key)


class GameDatabase(BaseDatabase):
    def __init__(self, filename):
        super().__init__(filename, "GRY", "gatunki_gier.txt")

    def load_games_data(self):
        return self._load_data("Producent")

    def remove_game(self, key):
        self.remove_entry(key)


class BookDatabase(BaseDatabase):
    def __init__(self, filename):
        super().__init__(filename, "KSIAZKI", "gatunki_ksiazek.txt")

    def load_books_data(self):
        return self._load_data("Autor")

    def remove_book(self, key):
        self.remove_entry(key)

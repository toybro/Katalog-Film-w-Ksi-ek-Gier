import tkinter as tk
from tkinter import ttk
import baza_danych_loading

# Importujemy funkcje z nowych, oddzielnych plików
from okno_szczegoly_filmy import otworz_okno_szczegoly
from okno_opinie_filmy import otworz_okno_opinie
from okno_dodaj_filmy import otworz_okno_dodaj


def powrotglowne(root, nowe_okno):
    nowe_okno.destroy()
    root.deiconify()


def laduj_lini(scrollable_frame, films_katalog, films_obj):
    # Czyścimy starą listę przed ponownym załadowaniem
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    for i in films_katalog.keys():
        text_str = f'{i}. {films_katalog[i]["Tytuł"]}, {films_katalog[i]["Rok"]}, {films_katalog[i].get("Reżyser", "Nieznany")}, {films_katalog[i]["Ocena"]}.'
        item_frame = tk.Frame(scrollable_frame, bg='lightyellow')
        item_frame.pack(fill='x', pady=2)

        label = tk.Label(item_frame, text=text_str, anchor='w', justify='left', bg='lightyellow')
        label.pack(side='left', padx=5, fill='x', expand=True)

        btn_frame = tk.Frame(item_frame, bg='lightyellow')
        btn_frame.pack(side='right', padx=5, fill='y')

        # Przycisk USUŃ
        usun_btn = tk.Button(btn_frame, text='Usuń',
                             command=lambda i=i, frame=item_frame, sf=scrollable_frame: usun_linie(i, frame, sf,
                                                                                                   films_obj))
        usun_btn.pack(side='right', padx=2)

        # Przycisk OPINIE
        opinie_btn = tk.Button(btn_frame, text='Opinie', width=8,
                               command=lambda i=i: otworz_okno_opinie(i, films_katalog))
        opinie_btn.pack(side='right', padx=2)

        # Przycisk SZCZEGÓŁY
        btn = tk.Button(btn_frame, text='Szczegóły', width=10,
                        command=lambda i=i: otworz_okno_szczegoly(i, films_katalog))
        btn.pack(side='right', padx=2)


def usun_linie(i, frame, scrollable_frame, films_obj):
    projekt.MovieDatabase.remove_movie(films_obj, i)
    films_katalog = films_obj.load_flms_data()
    frame.destroy()
    # Przeładowuje listę
    laduj_lini(scrollable_frame, films_katalog, films_obj)


def otworz_okno_filmy(root):
    root.withdraw()
    nowe_okno = tk.Toplevel(root)

    try:
        films = projekt.MovieDatabase(r"FILMY/baza_filmow.txt")
        films_katalog = films.load_flms_data()
        baza_istnieje = getattr(projekt.MovieDatabase, 'database_exist', True)
    except Exception as e:
        print(f"Błąd podczas ładowania bazy: {e}")
        baza_istnieje = False

    if baza_istnieje:
        nowe_okno.title("Katalog Filmów")
        nowe_okno.geometry("800x600")

        frame2 = tk.Frame(nowe_okno)
        # Zostawiamy miejsce na dole na przyciski Powrót i Dodaj
        frame2.pack(fill='both', expand=True, pady=(0, 50))

        canvas_list = tk.Canvas(frame2)
        scrollbar = ttk.Scrollbar(frame2, orient='vertical', command=canvas_list.yview)
        scrollable_frame = tk.Frame(canvas_list)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_list.configure(scrollregion=canvas_list.bbox("all"))
        )

        canvas_list.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas_list.configure(yscrollcommand=scrollbar.set)

        canvas_list.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        laduj_lini(scrollable_frame, films_katalog, films)

    else:
        nowe_okno.title("Komunikat")
        nowe_okno.geometry("300x200")
        label = tk.Label(nowe_okno, text="UWAGA!\nBaza filmów nie istnieje!\nUtworzono pustą Bazę filmów!")
        label.pack(pady=20)
        if hasattr(projekt.MovieDatabase, 'database_exist'):
            projekt.MovieDatabase.database_exist = True

    # -- DOLNA RAMKA NA PRZYCISKI POWRÓT i DODAJ --
    button_frame = tk.Frame(nowe_okno)
    button_frame.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Przycisk Powrót
    switch_button = tk.Button(button_frame, text="Powrót", font=("Arial", 12),
                              command=lambda: powrotglowne(root, nowe_okno))
    switch_button.pack(side='right', padx=5)

    # Przycisk Dodaj
    dodaj_button = tk.Button(button_frame, text="Dodaj", font=("Arial", 12),
                             command=lambda: otworz_okno_dodaj(films, scrollable_frame, laduj_lini))
    dodaj_button.pack(side='right', padx=5)

    nowe_okno.protocol("WM_DELETE_WINDOW", lambda: powrotglowne(root, nowe_okno))
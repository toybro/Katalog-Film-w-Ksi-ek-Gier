import tkinter as tk
from tkinter import ttk
import baza_danych_loading as projekt

from okno_szczegoly_ksiazki import otworz_okno_szczegoly
from okno_opinie_ksiazki import otworz_okno_opinie
from okno_dodaj_ksiazki import otworz_okno_dodaj


def powrotglowne(root, nowe_okno):
    nowe_okno.destroy()
    root.deiconify()


def laduj_linie(scrollable_frame, books_katalog, books_obj):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    for i in books_katalog.keys():
        text_str = (
            f"{i}. {books_katalog[i]['Tytuł']}, {books_katalog[i]['Rok']}, "
            f"{books_katalog[i].get('Autor', 'Nieznany')}, {books_katalog[i]['Ocena']}."
        )
        item_frame = tk.Frame(scrollable_frame, bg="lightyellow")
        item_frame.pack(fill="x", pady=2)

        tk.Label(item_frame, text=text_str, anchor="w", justify="left", bg="lightyellow").pack(
            side="left", padx=5, fill="x", expand=True
        )

        btn_frame = tk.Frame(item_frame, bg="lightyellow")
        btn_frame.pack(side="right", padx=5, fill="y")

        tk.Button(
            btn_frame,
            text="Usuń",
            command=lambda i=i, frame=item_frame, sf=scrollable_frame: usun_linie(i, frame, sf, books_obj),
        ).pack(side="right", padx=2)

        tk.Button(btn_frame, text="Opinie", width=8, command=lambda i=i: otworz_okno_opinie(i, books_katalog)).pack(
            side="right", padx=2
        )

        tk.Button(btn_frame, text="Szczegóły", width=10, command=lambda i=i: otworz_okno_szczegoly(i, books_katalog)).pack(
            side="right", padx=2
        )


def usun_linie(i, frame, scrollable_frame, books_obj):
    books_obj.remove_book(i)
    books_katalog = books_obj.load_books_data()
    frame.destroy()
    laduj_linie(scrollable_frame, books_katalog, books_obj)


def otworz_okno_ksiazki(root):
    root.withdraw()
    nowe_okno = tk.Toplevel(root)

    try:
        books = projekt.BookDatabase("KSIAZKI/baza_ksiazek.txt")
        books_katalog = books.load_books_data()
        baza_istnieje = getattr(projekt.BookDatabase, "database_exist", True)
    except Exception as e:
        print(f"Błąd podczas ładowania bazy książek: {e}")
        baza_istnieje = False

    if baza_istnieje:
        nowe_okno.title("Katalog Książek")
        nowe_okno.geometry("800x600")

        frame2 = tk.Frame(nowe_okno)
        frame2.pack(fill="both", expand=True, pady=(0, 50))

        canvas_list = tk.Canvas(frame2)
        scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=canvas_list.yview)
        scrollable_frame = tk.Frame(canvas_list)

        scrollable_frame.bind("<Configure>", lambda e: canvas_list.configure(scrollregion=canvas_list.bbox("all")))

        canvas_list.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas_list.configure(yscrollcommand=scrollbar.set)

        canvas_list.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        laduj_linie(scrollable_frame, books_katalog, books)
    else:
        nowe_okno.title("Komunikat")
        nowe_okno.geometry("300x200")
        tk.Label(nowe_okno, text="UWAGA!\nBaza książek nie istnieje!\nUtworzono pustą bazę książek!").pack(pady=20)
        if hasattr(projekt.BookDatabase, "database_exist"):
            projekt.BookDatabase.database_exist = True

    button_frame = tk.Frame(nowe_okno)
    button_frame.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    tk.Button(button_frame, text="Powrót", font=("Arial", 12), command=lambda: powrotglowne(root, nowe_okno)).pack(
        side="right", padx=5
    )

    if baza_istnieje:
        tk.Button(
            button_frame,
            text="Dodaj",
            font=("Arial", 12),
            command=lambda: otworz_okno_dodaj(books, scrollable_frame, laduj_linie),
        ).pack(side="right", padx=5)

    nowe_okno.protocol("WM_DELETE_WINDOW", lambda: powrotglowne(root, nowe_okno))

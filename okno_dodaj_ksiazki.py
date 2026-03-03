import tkinter as tk
from tkinter import messagebox


def _wczytaj_gatunki(sciezka="KSIAZKI/gatunki_ksiazek.txt"):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except OSError:
        return []


def zapisz_ksiazke(okno, tytul_entry, rok_entry, autor_entry, ocena_entry, opis_text, gatunek_var, books_obj,
                  scrollable_frame, funkcja_odswiezajaca):
    tytul = tytul_entry.get().strip()
    rok = rok_entry.get().strip()
    autor = autor_entry.get().strip()
    ocena = ocena_entry.get().strip() or "Brak oceny"
    opis = opis_text.get("1.0", tk.END).strip()
    gatunek = gatunek_var.get() or "[Brak gatunku]"

    if not tytul or not rok or not autor:
        messagebox.showwarning("Brak danych", "Pola: Tytuł, Rok i Autor są obowiązkowe!", parent=okno)
        return

    nowa_linia = f"{tytul};{rok};{autor};[{gatunek}];{ocena};{opis};[]\n"
    with open("KSIAZKI/baza_ksiazek.txt", "a", encoding="utf-8") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(nowa_linia.strip())

    books_katalog = books_obj.load_books_data()
    funkcja_odswiezajaca(scrollable_frame, books_katalog, books_obj)
    messagebox.showinfo("Sukces", "Książka została dodana.")
    okno.destroy()


def otworz_okno_dodaj(books_obj, scrollable_frame, funkcja_odswiezajaca):
    nowe_okno = tk.Toplevel()
    nowe_okno.title("Dodaj nową książkę")
    nowe_okno.geometry("520x520")

    form = tk.Frame(nowe_okno)
    form.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(form, text="Tytuł:").grid(row=0, column=0, sticky="e", pady=5)
    tytul_entry = tk.Entry(form, width=36)
    tytul_entry.grid(row=0, column=1, sticky="w")

    tk.Label(form, text="Rok:").grid(row=1, column=0, sticky="e", pady=5)
    rok_entry = tk.Entry(form, width=36)
    rok_entry.grid(row=1, column=1, sticky="w")

    tk.Label(form, text="Autor:").grid(row=2, column=0, sticky="e", pady=5)
    autor_entry = tk.Entry(form, width=36)
    autor_entry.grid(row=2, column=1, sticky="w")

    tk.Label(form, text="Ocena:").grid(row=3, column=0, sticky="e", pady=5)
    ocena_entry = tk.Entry(form, width=36)
    ocena_entry.grid(row=3, column=1, sticky="w")

    gatunki = _wczytaj_gatunki() or ["Brak"]
    tk.Label(form, text="Gatunek:").grid(row=4, column=0, sticky="e", pady=5)
    gatunek_var = tk.StringVar(value=gatunki[0])
    tk.OptionMenu(form, gatunek_var, *gatunki).grid(row=4, column=1, sticky="w")

    tk.Label(form, text="Opis:").grid(row=5, column=0, sticky="ne", pady=5)
    opis_text = tk.Text(form, width=36, height=8)
    opis_text.grid(row=5, column=1, sticky="w")

    tk.Button(
        nowe_okno,
        text="Zapisz książkę",
        command=lambda: zapisz_ksiazke(
            nowe_okno, tytul_entry, rok_entry, autor_entry, ocena_entry, opis_text, gatunek_var,
            books_obj, scrollable_frame, funkcja_odswiezajaca
        ),
    ).pack(side="left", padx=20, pady=12)
    tk.Button(nowe_okno, text="Anuluj", command=nowe_okno.destroy).pack(side="right", padx=20, pady=12)

import tkinter as tk
from tkinter import messagebox, ttk


def _wczytaj_gatunki(sciezka="KSIAZKI/gatunki_ksiazek.txt"):
    try:
        with open(sciezka, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except OSError:
        return []


def _pobierz_zaznaczone_gatunki(zmienne_gatunkow):
    zaznaczone = [gatunek for gatunek, var in zmienne_gatunkow.items() if var.get() == 1]
    if not zaznaczone:
        return "[Brak gatunku]"
    return "[" + ", ".join(zaznaczone) + "]"


def zapisz_ksiazke(okno, tytul_entry, rok_entry, autor_entry, ocena_entry, opis_text, zmienne_gatunkow, books_obj,
                  scrollable_frame, funkcja_odswiezajaca):
    tytul = tytul_entry.get().strip()
    rok = rok_entry.get().strip()
    autor = autor_entry.get().strip()
    ocena = ocena_entry.get().strip() or "Brak oceny"
    opis = opis_text.get("1.0", tk.END).strip()
    gatunek = _pobierz_zaznaczone_gatunki(zmienne_gatunkow)

    if not tytul or not rok or not autor:
        messagebox.showwarning("Brak danych", "Pola: Tytuł, Rok i Autor są obowiązkowe!", parent=okno)
        return

    nowa_linia = f"{tytul};{rok};{autor};{gatunek};{ocena};{opis};[]\n"
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
    nowe_okno.geometry("560x600")

    form = tk.Frame(nowe_okno)
    form.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(form, text="Tytuł:").grid(row=0, column=0, sticky="e", pady=5)
    tytul_entry = tk.Entry(form, width=40)
    tytul_entry.grid(row=0, column=1, sticky="w")

    tk.Label(form, text="Rok:").grid(row=1, column=0, sticky="e", pady=5)
    rok_entry = tk.Entry(form, width=40)
    rok_entry.grid(row=1, column=1, sticky="w")

    tk.Label(form, text="Autor:").grid(row=2, column=0, sticky="e", pady=5)
    autor_entry = tk.Entry(form, width=40)
    autor_entry.grid(row=2, column=1, sticky="w")

    tk.Label(form, text="Ocena:").grid(row=3, column=0, sticky="e", pady=5)
    ocena_entry = tk.Entry(form, width=40)
    ocena_entry.grid(row=3, column=1, sticky="w")

    tk.Label(form, text="Gatunki:").grid(row=4, column=0, sticky="ne", pady=5)

    gatunki_container = tk.Frame(form, bd=1, relief="sunken", bg="white")
    gatunki_container.grid(row=4, column=1, sticky="w", pady=5)

    gatunki_canvas = tk.Canvas(gatunki_container, height=130, width=300, bg="white")
    gatunki_scrollbar = ttk.Scrollbar(gatunki_container, orient="vertical", command=gatunki_canvas.yview)
    gatunki_inner = tk.Frame(gatunki_canvas, bg="white")

    gatunki_inner.bind("<Configure>", lambda e: gatunki_canvas.configure(scrollregion=gatunki_canvas.bbox("all")))
    gatunki_canvas.create_window((0, 0), window=gatunki_inner, anchor="nw")
    gatunki_canvas.configure(yscrollcommand=gatunki_scrollbar.set)

    gatunki_canvas.pack(side="left", fill="both", expand=True)
    gatunki_scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        gatunki_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    gatunki_canvas.bind("<Enter>", lambda e: gatunki_canvas.bind_all("<MouseWheel>", _on_mousewheel))
    gatunki_canvas.bind("<Leave>", lambda e: gatunki_canvas.unbind_all("<MouseWheel>"))

    zmienne_gatunkow = {}
    gatunki = _wczytaj_gatunki() or ["Brak"]
    for gatunek in gatunki:
        var = tk.IntVar()
        tk.Checkbutton(gatunki_inner, text=gatunek, variable=var, bg="white", anchor="w").pack(
            fill="x", padx=5, pady=2
        )
        zmienne_gatunkow[gatunek] = var

    tk.Label(form, text="Opis:").grid(row=5, column=0, sticky="ne", pady=5)
    opis_text = tk.Text(form, width=40, height=8)
    opis_text.grid(row=5, column=1, sticky="w")

    tk.Button(
        nowe_okno,
        text="Zapisz książkę",
        command=lambda: zapisz_ksiazke(
            nowe_okno, tytul_entry, rok_entry, autor_entry, ocena_entry, opis_text, zmienne_gatunkow,
            books_obj, scrollable_frame, funkcja_odswiezajaca
        ),
    ).pack(side="left", padx=20, pady=12)
    tk.Button(nowe_okno, text="Anuluj", command=nowe_okno.destroy).pack(side="right", padx=20, pady=12)

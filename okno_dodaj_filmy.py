import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os
import shutil

# Zmienna globalna do przechowywania ścieżki do wybranego obrazka
wybrana_sciezka_img = None


def wczytaj_gatunki(sciezka="FILMY/gatunki_filmow.txt"):
    """Pomocnicza funkcja do wczytania listy gatunków z pliku."""
    gatunki = []
    if os.path.exists(sciezka):
        try:
            with open(sciezka, "r", encoding="utf-8") as f:
                gatunki = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Błąd odczytu gatunków: {e}")
            return ["Błąd odczytu pliku gatunków"]
    else:
        return ["Brak pliku gatunki_filmow.txt"]
    return sorted(gatunki)


def wybierz_zdjecie(label_status):
    """Otwiera okno dialogowe wyboru pliku i aktualizuje etykietę."""
    global wybrana_sciezka_img
    filename = filedialog.askopenfilename(
        title="Wybierz okładkę filmu",
        filetypes=[("Pliki obrazów", "*.jpg *.jpeg *.png")]
    )
    if filename:
        wybrana_sciezka_img = filename
        nazwa_pliku = os.path.basename(filename)
        label_status.config(text=f"Wybrano: {nazwa_pliku}", fg="green")
    else:
        wybrana_sciezka_img = None
        label_status.config(text="Brak wybranego zdjęcia", fg="gray")


def zapisz_film(okno, tytul_entry, rok_entry, rezyser_entry, ocena_entry, opis_text, zmienne_gatunkow, films_obj,
                scrollable_frame, funkcja_odswiezajaca):
    global wybrana_sciezka_img

    tytul = tytul_entry.get().strip()
    rok = rok_entry.get().strip()
    rezyser = rezyser_entry.get().strip()
    ocena = ocena_entry.get().strip()
    opis = opis_text.get("1.0", tk.END).strip()

    zaznaczone_gatunki = []
    for gatunek, var in zmienne_gatunkow.items():
        if var.get() == 1:
            zaznaczone_gatunki.append(gatunek)

    if not tytul or not rok or not rezyser:
        messagebox.showwarning("Brak danych", "Pola: Tytuł, Rok i Reżyser są obowiązkowe!", parent=okno)
        return

    if not ocena:
        ocena = "Brak oceny"

    if not zaznaczone_gatunki:
        sformatowane_gatunki = "[Brak gatunku]"
    else:
        sformatowane_gatunki = "[" + ", ".join(zaznaczone_gatunki) + "]"

    opinie_puste = "[]"

    nowa_linia = f"{tytul};{rok};{rezyser};{sformatowane_gatunki};{ocena};{opis};{opinie_puste}\n"

    try:
        with open(r"FILMY/baza_filmow.txt", "a", encoding="utf-8") as file:
            file.write("\n" + nowa_linia.strip())

        if wybrana_sciezka_img:
            os.makedirs("FILMY", exist_ok=True)
            sciezka_docelowa = os.path.join("FILMY", f"{tytul}.jpg")
            shutil.copyfile(wybrana_sciezka_img, sciezka_docelowa)

        films_katalog = films_obj.load_flms_data()
        funkcja_odswiezajaca(scrollable_frame, films_katalog, films_obj)

        messagebox.showinfo("Sukces", "Film został pomyślnie dodany do bazy!")
        wybrana_sciezka_img = None
        okno.destroy()

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem przy zapisywaniu filmu:\n{e}", parent=okno)


def otworz_okno_dodaj(films_obj, scrollable_frame, funkcja_odswiezajaca):
    global wybrana_sciezka_img
    wybrana_sciezka_img = None

    nowe_okno = tk.Toplevel()
    nowe_okno.title("Dodaj nowy film")
    nowe_okno.geometry("550x700")

    label = tk.Label(nowe_okno, text="Formularz dodawania filmu", font=("Arial", 16, "bold"))
    label.pack(pady=15)

    form_frame = tk.Frame(nowe_okno)
    form_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # 1. Tytuł
    tk.Label(form_frame, text="Tytuł (wymagane):", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="e", pady=5)
    tytul_entry = tk.Entry(form_frame, width=40, font=("Arial", 10))
    tytul_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

    # 2. Rok
    tk.Label(form_frame, text="Rok wydania (wymagane):", font=("Arial", 11)).grid(row=1, column=0, sticky="e", pady=5)
    rok_entry = tk.Entry(form_frame, width=40, font=("Arial", 10))
    rok_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

    # 3. Reżyser
    tk.Label(form_frame, text="Reżyser (wymagane):", font=("Arial", 11)).grid(row=2, column=0, sticky="e", pady=5)
    rezyser_entry = tk.Entry(form_frame, width=40, font=("Arial", 10))
    rezyser_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

    # 4. Ocena
    tk.Label(form_frame, text="Ocena (np. 8.5):", font=("Arial", 11)).grid(row=3, column=0, sticky="e", pady=5)
    ocena_entry = tk.Entry(form_frame, width=40, font=("Arial", 10))
    ocena_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

    # 5. Zdjęcie
    tk.Label(form_frame, text="Okładka (opcjonalne):", font=("Arial", 11)).grid(row=4, column=0, sticky="e", pady=15)
    img_frame = tk.Frame(form_frame)
    img_frame.grid(row=4, column=1, sticky="w", padx=10, pady=15)
    img_status_label = tk.Label(img_frame, text="Brak wybranego zdjęcia", fg="gray", font=("Arial", 9))
    wybierz_btn = tk.Button(img_frame, text="Wybierz plik...", font=("Arial", 9),
                            command=lambda: wybierz_zdjecie(img_status_label))
    wybierz_btn.pack(side="left")
    img_status_label.pack(side="left", padx=10)

    # 6. GATUNKI (Checkboxy ze scrollem i obsługą rolki myszy)
    tk.Label(form_frame, text="Gatunki:", font=("Arial", 11)).grid(row=5, column=0, sticky="ne", pady=5)

    genres_container = tk.Frame(form_frame, bd=1, relief="sunken", bg="white")
    genres_container.grid(row=5, column=1, sticky="w", padx=10, pady=5)

    genres_canvas = tk.Canvas(genres_container, height=120, width=280, bg="white")
    genres_scrollbar = ttk.Scrollbar(genres_container, orient="vertical", command=genres_canvas.yview)
    genres_inner_frame = tk.Frame(genres_canvas, bg="white")

    genres_inner_frame.bind(
        "<Configure>",
        lambda e: genres_canvas.configure(scrollregion=genres_canvas.bbox("all"))
    )
    genres_canvas.create_window((0, 0), window=genres_inner_frame, anchor="nw")
    genres_canvas.configure(yscrollcommand=genres_scrollbar.set)

    genres_canvas.pack(side="left", fill="both", expand=True)
    genres_scrollbar.pack(side="right", fill="y")


    def _on_mousewheel(event):
        genres_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    genres_canvas.bind('<Enter>', lambda e: genres_canvas.bind_all("<MouseWheel>", _on_mousewheel))
    genres_canvas.bind('<Leave>', lambda e: genres_canvas.unbind_all("<MouseWheel>"))

    lista_gatunkow = wczytaj_gatunki()
    zmienne_gatunkow = {}

    for gatunek in lista_gatunkow:
        var = tk.IntVar()
        cb = tk.Checkbutton(genres_inner_frame, text=gatunek, variable=var, bg="white", anchor="w")
        cb.pack(fill="x", padx=5, pady=2)
        zmienne_gatunkow[gatunek] = var

    # 7. Opis
    tk.Label(form_frame, text="Opis:", font=("Arial", 11)).grid(row=6, column=0, sticky="ne", pady=15)
    opis_text = tk.Text(form_frame, width=40, height=6, font=("Arial", 10))
    opis_text.grid(row=6, column=1, pady=15, padx=10, sticky="w")

    # PRZYCISNK AKCJI
    btn_frame = tk.Frame(nowe_okno)
    btn_frame.pack(pady=10, side="bottom")

    zapisz_btn = tk.Button(btn_frame, text="Zapisz film", font=("Arial", 12, "bold"), bg="#90EE90", width=15,
                           command=lambda: zapisz_film(nowe_okno, tytul_entry, rok_entry, rezyser_entry,
                                                       ocena_entry, opis_text, zmienne_gatunkow,
                                                       films_obj, scrollable_frame, funkcja_odswiezajaca))
    zapisz_btn.pack(side="left", padx=10)

    anuluj_btn = tk.Button(btn_frame, text="Anuluj", font=("Arial", 12), width=15, command=nowe_okno.destroy)
    anuluj_btn.pack(side="left", padx=10)
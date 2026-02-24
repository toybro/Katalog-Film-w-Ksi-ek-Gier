import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys

# Upewnij się, że te pliki istnieją w tym samym katalogu
from okno_filmy import otworz_okno_filmy
from okno_gry import otworz_okno_gry
from okno_ksiazki import otworz_okno_ksiazki


def zakoncz_program(root):
    root.destroy()
    sys.exit()


def animate_text(canvas, text_id):
    global dx
    # Przesuwanie tekstu
    canvas.move(text_id, dx, 0)
    pos = canvas.coords(text_id)
    width = canvas.winfo_width()

    # Oblicz szerokość tekstu
    bbox = canvas.bbox(text_id)
    text_width = bbox[2] - bbox[0]

    # Odwróć kierunek, jeśli tekst wyszedł za granicę
    if pos[0] + text_width >= width or pos[0] <= 0:
        dx = -dx

    # Kontynuuj animację
    canvas.after(20, lambda: animate_text(canvas, text_id))


def main():
    global dx
    dx = 5

    root = tk.Tk()
    root.title("Biblioteka Danych")
    root.geometry("800x600")

    # Frame 1: Tekst poruszający się (Nagłówek)
    frame1 = tk.Frame(root, height=50)
    frame1.pack(fill='x')
    canvas = tk.Canvas(frame1, height=50)
    canvas.pack(fill='both', expand=True)
    text_id = canvas.create_text(5, 25, text="Zasoby główne", anchor='w', font=('Arial', 26))

    # Rozpoczęcie animacji po załadowaniu okna
    root.after(100, lambda: animate_text(canvas, text_id))

    # --- GŁÓWNA SEKCJA ---
    # Frame 2: Główny obszar roboczy, który zajmuje całe dostępne miejsce
    frame2 = tk.Frame(root)
    frame2.pack(fill='both', expand=True, padx=10, pady=10)

    # NOWOŚĆ: Kontener centrujący.
    # Tworzymy ramkę wewnątrz frame2, która będzie ciasno trzymać zawartość.
    # Użycie expand=True sprawi, że ten kontener zostanie wyśrodkowany wewnątrz frame2.
    content_container = tk.Frame(frame2)
    content_container.pack(expand=True)

    # Wczytanie obrazków (obsługa błędów, jeśli plików nie ma)
    try:
        img1 = Image.open("img1.png").resize((100, 105))
        img2 = Image.open("img2.png").resize((100, 150))
        img3 = Image.open("img3.png").resize((100, 150))
        photo1 = ImageTk.PhotoImage(img1)
        photo2 = ImageTk.PhotoImage(img2)
        photo3 = ImageTk.PhotoImage(img3)
        btn_images = [photo1, photo2, photo3]
    except FileNotFoundError:
        print("Brak plików graficznych (img1.png, img2.png, img3.png). Guziki będą bez obrazków.")
        btn_images = [None, None, None]

    # Tworzenie przycisków w pętli
    commands = [
        lambda: otworz_okno_filmy(root),
        lambda: otworz_okno_gry(root),
        lambda: otworz_okno_ksiazki(root)
    ]
    texts = ["Katalog filmów", "Katalog Gier", "Katalog książek"]

    for i in range(3):
        # ZMIANA: Rodzicem dla rzędu jest teraz content_container, a nie frame2.
        row = tk.Frame(content_container)
        # USUNIĘTO fill='x', aby rząd dopasował się do zawartości.
        # Zwiększono pady dla lepszego odstępu między rzędami.
        row.pack(pady=15)

        # Obrazek po lewej (jeśli istnieje)
        if btn_images[i]:
            lbl = tk.Label(row, image=btn_images[i])
            lbl.image = btn_images[i]  # Zachowanie referencji
            lbl.pack(side='left', padx=(0, 10))  # Dodatkowy odstęp po prawej stronie obrazka

        btn = tk.Button(row, text=texts[i], font=("Arial", 14), width=20, command=commands[i])
        btn.pack(side='left')

    # --- STOPKI I PRZYCISK WYJŚCIA ---
    stopka_frame = tk.Frame(root)
    stopka_frame.pack(side="bottom", fill="x", pady=10)

    stopka2 = tk.Label(stopka_frame, text="SEBA KRZYCH", font=("Arial", 12))
    stopka2.pack(side="bottom")
    stopka = tk.Label(stopka_frame, text="KOPY RAJT", font=("Arial", 12))
    stopka.pack(side="bottom")

    # Przycisk w prawym dolnym rogu
    button_frame = tk.Frame(root)
    button_frame.place(relx=1.0, rely=1.0, anchor='se')
    switch_button = tk.Button(button_frame, text="Wyjście", font=('Arial', 14), command=lambda: zakoncz_program(root))
    switch_button.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
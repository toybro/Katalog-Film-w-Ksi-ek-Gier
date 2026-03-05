import tkinter as tk


def otworz_okno_szczegoly(index, books_katalog):
    new_win = tk.Toplevel()
    new_win.title("Szczegóły książki")
    new_win.geometry("700x450")

    book = books_katalog[index]

    tk.Label(new_win, text=book["Tytuł"], font=("Arial", 18, "bold"), fg="blue").pack(pady=8)
    tk.Label(new_win, text=f"Rok: {book['Rok']}", font=("Arial", 12)).pack()
    tk.Label(new_win, text=f"Autor: {book.get('Autor', 'Nieznany')}", font=("Arial", 12)).pack()
    tk.Label(new_win, text=f"Ocena: {book['Ocena']}", font=("Arial", 12)).pack(pady=3)
    tk.Label(new_win, text=f"Gatunek: {book.get('Gatunek', 'Brak gatunku')}", font=("Arial", 11, "italic")).pack(pady=5)

    opis = book.get("Opis", "Brak opisu")
    msg = tk.Message(new_win, text=opis, width=620, font=("Arial", 11), justify="left")
    msg.pack(fill="x", padx=16, pady=10)

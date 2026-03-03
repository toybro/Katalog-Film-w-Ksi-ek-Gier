import tkinter as tk


def otworz_okno_szczegoly(index, games_katalog):
    new_win = tk.Toplevel()
    new_win.title("Szczegóły gry")
    new_win.geometry("700x450")

    game = games_katalog[index]

    tk.Label(new_win, text=game["Tytuł"], font=("Arial", 18, "bold"), fg="blue").pack(pady=8)
    tk.Label(new_win, text=f"Rok: {game['Rok']}", font=("Arial", 12)).pack()
    tk.Label(new_win, text=f"Producent: {game.get('Producent', 'Nieznany')}", font=("Arial", 12)).pack()
    tk.Label(new_win, text=f"Ocena: {game['Ocena']}", font=("Arial", 12)).pack(pady=3)
    tk.Label(new_win, text=f"Gatunek: {game.get('Gatunek', 'Brak gatunku')}", font=("Arial", 11, "italic")).pack(pady=5)

    opis = game.get("Opis", "Brak opisu")
    msg = tk.Message(new_win, text=opis, width=620, font=("Arial", 11), justify="left")
    msg.pack(fill="x", padx=16, pady=10)

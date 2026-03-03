import tkinter as tk


def powrotglowne(root, nowe_okno):
    nowe_okno.destroy()
    root.deiconify()


def otworz_okno_gry(root):
    # Ukrywa okno główne (main.py)
    root.withdraw()

    nowe_okno = tk.Toplevel(root)
    nowe_okno.title("Katalog Gier")
    nowe_okno.geometry("400x300")

    # Przycisk "Powrót" wykorzystujący funkcję przywracającą okno główne
    powrot = tk.Button(nowe_okno, text="Powrót", font=("Arial", 14), command=lambda: powrotglowne(root, nowe_okno))
    powrot.pack(pady=40)

    # Zabezpieczenie: przywraca główne okno, gdy użytkownik zamknie to okno "krzyżykiem" (prawy górny róg)
    nowe_okno.protocol("WM_DELETE_WINDOW", lambda: powrotglowne(root, nowe_okno))
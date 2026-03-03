import tkinter as tk


def otworz_okno_opinie(index, books_katalog):
    nowe_okno = tk.Toplevel()
    nowe_okno.title("Opinie o książce")
    nowe_okno.geometry("400x300")

    tytul = books_katalog[index]["Tytuł"]

    label = tk.Label(nowe_okno, text=f"Opinie dla: {tytul}", font=("Arial", 16, "bold"))
    label.pack(pady=20)

    info = tk.Label(nowe_okno, text="Tutaj w przyszłości pojawi się system opinii.")
    info.pack(pady=10)

    zamknij = tk.Button(nowe_okno, text="Zamknij", command=nowe_okno.destroy)
    zamknij.pack(pady=20)

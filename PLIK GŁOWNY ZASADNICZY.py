import tkinter as tk

root = tk.Tk()
root.title("Biblioteka Danych")
root.geometry("800x600")

label = tk.Label(root, text="Zasoby główne", font=("Arial", 26))
stopka = tk.Label(root, text="KOPY RAJT", font=("Arial", 12))
stopka2 = tk.Label(root, text="SEBA KRZYCH", font=("Arial", 12))
label.pack(pady=50)
stopka2.pack(side="bottom")
stopka.pack(side="bottom")

#FUNKCJE PROGRAMH DO OKIEN

def klikkataloggry():
    nowe_okno = tk.Toplevel(root)
    nowe_okno.title("Katalog Gier")
    nowe_okno.geometry("400x300")

    powrot = tk.Button(nowe_okno, text="Powrót", font=("Arial", 14), command=nowe_okno.destroy)
    powrot.pack(pady=40)

def klikkatalogfilmy():
    nowe_okno = tk.Toplevel(root)
    nowe_okno.title("Katalog Filmów")
    nowe_okno.geometry("400x300")

    powrot = tk.Button(nowe_okno, text="Powrót", font=("Arial", 14), command=nowe_okno.destroy)
    powrot.pack(pady=40)

def klikkatalogksiazki():
    nowe_okno = tk.Toplevel(root)
    nowe_okno.title("Katalog Książek")
    nowe_okno.geometry("400x300")

    powrot = tk.Button(nowe_okno, text="Powrót", font=("Arial", 14), command=nowe_okno.destroy)
    powrot.pack(pady=40)


def klik():

    pass

def klik():

    pass


#BUTONY

siatka_guzikuw = tk.Frame(root)
siatka_guzikuw.pack(pady=1)

filmyklik = tk.Button(siatka_guzikuw, text="Katalog filmów", command=klikkatalogfilmy, font=("Arial", 14))
gryklik = tk.Button(siatka_guzikuw, text="Katalog Gier", command=klikkataloggry, font=("Arial", 14))
ksiazklik = tk.Button(siatka_guzikuw, text="Katalog książek", command=klikkatalogksiazki, font=("Arial", 14))

filmyklik.grid(row=0, column=0, padx=10, pady=3, sticky="w")
gryklik.grid(row=1, column=0, padx=10, pady=3, sticky="w")
ksiazklik.grid(row=2, column=0, padx=10, pady=3, sticky="w")

root.mainloop()
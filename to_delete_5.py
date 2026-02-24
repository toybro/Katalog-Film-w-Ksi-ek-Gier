import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import projekt
 
films = projekt.MovieDatabase(r"FILMY/baza_filmow.txt") # nie wiem, czy w dobrym miejscu się znajduje
films_katalog = films.load_flms_data()
 
labels = []
def open_line_window(index):  # dopracować, aby szczegóły się wyświetlały i opinie i oceny
    global new_root
    # new_root.withdraw()
 
    new_win = tk.Toplevel()
    new_win.title("Szczegóły filmu")
    new_win.geometry("800x600")
 
    title_movie = films_katalog[index]["Tytuł"]
    year_movie = films_katalog[index]["Rok"]
    rating_movie = films_katalog[index]["Ocena"]
 
    top_frame = tk.Frame(new_win)
    top_frame.pack()
    title_label_1 = tk.Label(top_frame, text="Tytuł:  ", font=("Arial", 12, "italic"), fg="black")
    title_label_1.pack(side=tk.LEFT, pady=1)
    title_label = tk.Label(top_frame, text=title_movie, font=("Arial", 18, "bold"), fg="blue")
    title_label.pack(pady=1)
 
    top_frame_2 = tk.Frame(new_win)
    top_frame_2.pack(pady=1)  
    year_label = tk.Label(top_frame_2, text="Rok:  ", font=("Arial", 12, "italic"), fg="black")
    year_label.pack(side=tk.LEFT, pady=1)
    year_label = tk.Label(top_frame_2, text=year_movie, font=("Arial", 16), fg="gray")
    year_label.pack(pady=1)
 
    top_frame_3 = tk.Frame(new_win)
    top_frame_3.pack()  
    year_label = tk.Label(top_frame_3, text="Ocena:  ", font=("Arial", 12, "italic"), fg="black")
    year_label.pack(side=tk.LEFT)
    year_label = tk.Label(top_frame_3, text=rating_movie, font=("Arial", 14), fg="black")
    year_label.pack()
 
    main_frame = tk.Frame(new_win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)
 
    try:
        img_title = films_katalog[index]["Tytuł"]
        img_path = r"FILMY/" + img_title + ".jpg"
        img = Image.open(img_path)
        img = img.resize((200, 300))
        photo = ImageTk.PhotoImage(img)
    except FileNotFoundError:
        # Ścieżka do standardowego obrazu
        standard_img_path = r"FILMY/Empty.jpg"
        img = Image.open(standard_img_path)
        img = img.resize((200, 300))
        photo = ImageTk.PhotoImage(img)
 
    img_label = tk.Label(main_frame, image=photo)
    img_label.image = photo
    img_label.pack(side='left', padx=10)
   
    # Opis po prawej
    description_frame = tk.Frame(main_frame)
    description_frame.pack(side='left', fill='both', expand=True)
 
    description_movie = films_katalog[index]["Opis"]
    genre_movie = films_katalog[index]["Gatunek"]
   
    # Opis i gatunek
    description_label = tk.Label(description_frame, text=description_movie, justify='left', wraplength=400)
    description_label.pack(pady=10)
 
    genre_label = tk.Label(description_frame, text=genre_movie, font=("Arial", 12, "italic"))
    genre_label.pack(pady=5)
   
    # Paski przewijania pod całością - z opiniami i guzik dodaj opinię
    # Tworzymy Canvas do przewijania
    canvas = tk.Canvas(new_win)
    scrollbar = ttk.Scrollbar(new_win, orient='vertical', command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
 
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
 
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)
 
    # Umieść główny ramka i scrollbar w głównym oknie
    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
 
def laduj_lini(frame, scrollable_frame):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
 
    for i in films_katalog.keys():
        text_str = f'{i}. {films_katalog[i]["Tytuł"]}, {films_katalog[i]["Rok"]}, {films_katalog[i]["Reżyser"]}, {films_katalog[i]["Ocena"]}.'
        item_frame = tk.Frame(scrollable_frame, bg='lightyellow')  # zmień kolor
        item_frame.pack(fill='x', pady=2)
        label = tk.Label(item_frame, text=text_str, anchor='w', justify='left', bg='lightyellow')
        label.pack(side='left', padx=5, fill='x', expand=True)
        labels.append(label)
 
        btn_frame = tk.Frame(item_frame, bg='lightyellow')
        btn_frame.pack(side='right', padx=5, fill='y')
 
        usun_btn = tk.Button(item_frame, text='Usuń', command=lambda i=i, frame=item_frame, sf=scrollable_frame: usun_linie(i, frame, sf))
        usun_btn.pack(side='right', padx=2)
 
        btn = tk.Button(item_frame, text='Szczegóły', width=10, command=lambda i=i: open_line_window(i))
        btn.pack(side='right', padx=10)
   
 
def usun_linie(i, frame, scrollable_frame):  # dopracować, aby nadpisywała się baza i pobierała raz jeszcze
    # trzeba dodać reload
    global films_katalog
    projekt.MovieDatabase.remove_movie(films, i)
    films_katalog = films.load_flms_data()
    frame.destroy()
    laduj_lini(frame.master, scrollable_frame)
 
def zakoncz_program():
    main_root.destroy()
    sys.exit()
 
def zadanie_guzik1():
    global films
    global main_root
    global new_root
   
    main_root.withdraw()
    new_root = tk.Toplevel()
   
    if projekt.MovieDatabase.database_exist == True:
        new_root.title("Nowe okno")
        new_root.geometry("800x600")
        frame2 = tk.Frame(new_root)
        frame2.pack(fill='both', expand=True)
        canvas_list = tk.Canvas(frame2)
        scrollbar = ttk.Scrollbar(frame2, orient='vertical', command=canvas_list.yview)
        scrollable_frame = tk.Frame(canvas_list)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_list.configure(
                scrollregion=canvas_list.bbox("all")))
       
        canvas_window = canvas_list.create_window((0, 0), window=scrollable_frame, anchor='nw') # chyba nie jest nigdzie używane
        canvas_list.configure(yscrollcommand=scrollbar.set)
 
        canvas_list.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
       
        laduj_lini(new_root, scrollable_frame)
       
    else:  
        new_root.title("Komunikat")
        new_root.geometry("300x200")
        label = tk.Label(new_root, text="UWAGA!\nBaza filmów nie istnieje!\nUtworzono pustą Bazę filmów!")
        label.pack(pady=20)
        projekt.MovieDatabase.database_exist = True
 
        # UwAGA - tu są inne powroty jak baza nie isnieje (jakieś dziwne rzeczy się dziej -
        # coś przerobić - ukrycie i powrót okna głównego:
        # coś w stylu : main_root.withdraw() oraz main_root.deiconify()
    button_frame = tk.Frame(new_root)
    button_frame.place(relx=1.0, rely=1.0, anchor='se')
    switch_button = tk.Button(button_frame, text="Powrót", command=lambda: return_to_main(new_root))
    switch_button.pack(padx=10, pady=10)
 
    new_root.mainloop()
 
 
def return_to_main(current_root):
    current_root.destroy()
    main_root.deiconify()
 
 
def zadanie_guzik2():
    print("Guzik 2 został kliknięty!")
    # tutaj możesz wpisać dowolne zadanie dla guzika 2
 
def zadanie_guzik3():
    print("Guzik 3 został kliknięty!")
    # tutaj możesz wpisać dowolne zadanie dla guzika 3
 
def animate_text():
    global text_id, dx
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
    canvas.after(20, animate_text)
 
def main():
    global main_root, canvas, text_id, dx
 
    main_root = tk.Tk()
    main_root.title("Biblioteka Danych")
    main_root.geometry("800x600")
 
    # Frame 1: Tekst poruszający się
    frame1 = tk.Frame(main_root, height=50)
    frame1.pack(fill='x')
    global canvas
    canvas = tk.Canvas(frame1, height=50)
    canvas.pack(fill='both', expand=True)
    text_id = canvas.create_text(5, 25, text="Zasoby główne", anchor='w', font=('Arial', 26))
    dx = 5
    animate_text()
 
    # Drugi frame na guziki i obrazki
    frame2 = tk.Frame(main_root)
    frame2.pack(fill='both', expand=True, padx=10, pady=10)
 
    # Wczytanie obrazków
    img1 = Image.open("img1.png").resize((100, 105))
    img2 = Image.open("img2.png").resize((100, 150))
    img3 = Image.open("img3.png").resize((100, 150))
    photo1 = ImageTk.PhotoImage(img1)
    photo2 = ImageTk.PhotoImage(img2)
    photo3 = ImageTk.PhotoImage(img3)
    btn_images = [photo1, photo2, photo3]
 
    # Tworzymy trzy wiersze, każdy z obrazkiem i guzikiem obok siebie
    for i, img in enumerate(btn_images):
        row = tk.Frame(frame2)
        row.pack(fill='x', pady=5)
 
        # Obrazek po lewej
        lbl = tk.Label(row, image=img)
        lbl.pack(side='left')
 
        # Guzik po prawej, z przypisaną funkcją
        if i == 0:
            command = zadanie_guzik1
        elif i == 1:
            command = zadanie_guzik2
        else:
            command = zadanie_guzik3
 
        btn = tk.Button(row, text=f"Guzik {i+1}", font=("Arial", 14), command=command)
        btn.pack(side='left', padx=10)
 
    # Tekst na dole na wysokości guzika
    dolny_frame = tk.Frame(main_root)
    dolny_frame.pack(fill='x', pady=20)
 
    # Dodanie etykiety z tekstem wyśrodkowanym
    dolny_tekst = tk.Label(dolny_frame, text="To jest tekst\n na dole, na środku", font=('Arial', 14))
    dolny_tekst.pack()
 
    # Frame 3: Przycisk w prawym dolnym rogu
    button_frame = tk.Frame(main_root)
    button_frame.place(relx=1.0, rely=1.0, anchor='se')
    switch_button = tk.Button(button_frame, text="Wyjście", font=('Arial', 14), command=zakoncz_program)
    switch_button.pack(padx=10, pady=10)
 
    main_root.mainloop()
 
if __name__ == "__main__":
    main()
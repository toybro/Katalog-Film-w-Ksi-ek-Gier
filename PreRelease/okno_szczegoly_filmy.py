import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def otworz_okno_szczegoly(index, films_katalog):
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
    year_label_1 = tk.Label(top_frame_2, text="Rok:  ", font=("Arial", 12, "italic"), fg="black")
    year_label_1.pack(side=tk.LEFT, pady=1)
    year_label = tk.Label(top_frame_2, text=year_movie, font=("Arial", 16), fg="gray")
    year_label.pack(pady=1)

    top_frame_3 = tk.Frame(new_win)
    top_frame_3.pack()
    rating_label_1 = tk.Label(top_frame_3, text="Ocena:  ", font=("Arial", 12, "italic"), fg="black")
    rating_label_1.pack(side=tk.LEFT)
    rating_label = tk.Label(top_frame_3, text=rating_movie, font=("Arial", 14), fg="black")
    rating_label.pack()

    main_frame = tk.Frame(new_win)
    main_frame.pack(fill='both', expand=True, padx=10, pady=10)

    try:
        img_title = films_katalog[index]["Tytuł"]
        img_path = r"FILMY/" + img_title + ".jpg"
        img = Image.open(img_path)
        img = img.resize((200, 300))
        photo = ImageTk.PhotoImage(img)
    except FileNotFoundError:
        try:
            standard_img_path = r"FILMY/Empty.jpg"
            img = Image.open(standard_img_path)
            img = img.resize((200, 300))
            photo = ImageTk.PhotoImage(img)
        except FileNotFoundError:
            photo = None

    if photo:
        img_label = tk.Label(main_frame, image=photo)
        img_label.image = photo
        img_label.pack(side='left', padx=10)
    else:
        img_label = tk.Label(main_frame, text="Brak okładki", width=25, height=15, bg="lightgray")
        img_label.pack(side='left', padx=10)

    description_frame = tk.Frame(main_frame)
    description_frame.pack(side='left', fill='both', expand=True)

    description_movie = films_katalog[index].get("Opis", "Brak opisu")
    genre_movie = films_katalog[index].get("Gatunek", "Brak gatunku")

    description_label = tk.Label(description_frame, text=description_movie, justify='left', wraplength=400)
    description_label.pack(pady=10)

    genre_label = tk.Label(description_frame, text=genre_movie, font=("Arial", 12, "italic"))
    genre_label.pack(pady=5)

    canvas = tk.Canvas(new_win)
    scrollbar = ttk.Scrollbar(new_win, orient='vertical', command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
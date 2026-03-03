import tkinter as tk
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
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        img_title = films_katalog[index]["Tytuł"]
        img_path = "FILMY/" + img_title + ".jpg"
        img = Image.open(img_path)
        img = img.resize((200, 300))
        photo = ImageTk.PhotoImage(img)
    except FileNotFoundError:
        try:
            standard_img_path = "FILMY/Empty.jpg"
            img = Image.open(standard_img_path)
            img = img.resize((200, 300))
            photo = ImageTk.PhotoImage(img)
        except FileNotFoundError:
            photo = None

    if photo:
        img_label = tk.Label(main_frame, image=photo)
        img_label.image = photo
        img_label.pack(side="left", padx=10)
    else:
        img_label = tk.Label(main_frame, text="Brak okładki", width=25, height=15, bg="lightgray")
        img_label.pack(side="left", padx=10)

    description_frame = tk.Frame(main_frame)
    description_frame.pack(side="left", fill="both", expand=True)

    description_movie = films_katalog[index].get("Opis", "Brak opisu")
    genre_movie = films_katalog[index].get("Gatunek", "Brak gatunku")

    # Opis w ramce
    description_box = tk.LabelFrame(description_frame, text="Opis", padx=10, pady=10)
    description_box.pack(fill="both", expand=True, pady=(10, 5))

    description_label = tk.Label(description_box, text=description_movie, justify="left", wraplength=400, anchor="nw")
    description_label.pack(fill="both", expand=True)

    # Gatunek pod ramką
    genre_label = tk.Label(description_frame, text=f"Gatunek: {genre_movie}", font=("Arial", 12, "italic"))
    genre_label.pack(anchor="w", pady=(6, 0), padx=2)

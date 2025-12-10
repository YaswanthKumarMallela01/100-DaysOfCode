from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = []
flip_timer = None
current_language = None

BACKGROUND_COLOR = "#B1DDC6"


def start_language(lang):
    global to_learn, flip_timer, current_language
    current_language = lang

    if flip_timer is not None:
        try:
            windows.after_cancel(flip_timer)
        except Exception:
            pass

    try:
        canvas.delete(language_text)
    except Exception:
        pass

    try:
        hindi_answer_button.destroy()
        french_answer_button.destroy()
    except Exception:
        pass

    if lang == "Hindi":
        base_name = "hindi_words"
    else:
        base_name = "french_words"

    try:
        data = pd.read_csv(f"./Data/{base_name}_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv(f"./Data/{base_name}.csv")

    to_learn = data.to_dict(orient="records")
    next_card()


def next_card():
    global current_card, flip_timer

    if flip_timer is not None:
        try:
            windows.after_cancel(flip_timer)
        except Exception:
            pass

    if not to_learn:
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text=current_language, fill="black")
    canvas.itemconfig(card_word, text=current_card[current_language], fill="black")
    flip_timer = windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)

    if current_language == "Hindi":
        file_name = "./Data/hindi_words_to_learn.csv"
    else:
        file_name = "./Data/french_words_to_learn.csv"

    data.to_csv(file_name, index=False)
    next_card()


windows = Tk()
windows.title("Flashy")
windows.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="./Images/card_back.png")
card_front_image = PhotoImage(file="./Images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

unknown_image = PhotoImage(file="./Images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_image = PhotoImage(file="./Images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

language_text = canvas.create_text(400, 50, text="What language do you want to learn?", font=("Arial", 20, "italic"))

hindi_image = PhotoImage(file="./Images/hindi.png")
french_image = PhotoImage(file="./Images/french.png")
hindi_answer_button = Button(image=hindi_image, highlightthickness=0, command=lambda: start_language("Hindi"))
french_answer_button = Button(image=french_image, highlightthickness=0, command=lambda: start_language("French"))
canvas.create_window(500, 200, window=hindi_answer_button)
canvas.create_window(300, 200, window=french_answer_button)

windows.mainloop()

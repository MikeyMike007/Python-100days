import tkinter as tk
import pandas as pd
import random
import time

current_card = {}
to_learn = {}


BACKGROUND_COLOR = "#B1DDC6"


# Data
# ----------------------
try:
    data = pd.read_csv("./data/words_to_learn")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data
else:
    to_learn = data

to_learn = data.to_dict(orient="records")
# Model
# --------------


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=img_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=img_back)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    # Do not include index
    data.to_clipboard("./data/words_to_learn.csv", index=False)


# UI
# -------------------------
window = tk.Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

img_front = tk.PhotoImage(file="./images/card_front.png")
img_back = tk.PhotoImage(file="./images/card_back.png")
img_wrong = tk.PhotoImage(file="./images/wrong.png")
img_right = tk.PhotoImage(file="./images/right.png")

btn_wrong = tk.Button(image=img_wrong, highlightthickness=0, bd=0, command=next_card)
btn_right = tk.Button(image=img_right, highlightthickness=0, bd=0, command=is_known)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_background = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial,", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial,", 40, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
btn_wrong.grid(row=1, column=0)
btn_right.grid(row=1, column=1)

next_card("pass")
window.mainloop()

from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "times new roman"
current_card = {}
to_learn = {}
# Dataframe
try:
    df = pd.read_csv(filepath_or_buffer="data/new_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


# Functions

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    Canvas.itemconfig(language_status, text="French", fill="black")
    Canvas.itemconfig(word_displayed, text=current_card["French"], fill="black")
    Canvas.itemconfig(background_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    Canvas.itemconfig(language_status, text="English", fill="white")
    Canvas.itemconfig(word_displayed, text=current_card["English"], fill="white")
    Canvas.itemconfig(background_image, image=card_back)


def known_word():
    to_learn.remove(current_card)
    generate_word()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/new_words.csv", index=False)

# UI setup
window = Tk()
window.title("flash card program")
window.config(bg=BACKGROUND_COLOR)
window.config(pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

Canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file='images/card_back.png')
background_image = Canvas.create_image(400, 264, image=card_front)
Canvas.grid(row=1, column=1)

# buttons
x_mark = PhotoImage(file="images/wrong.png")
check_mark = PhotoImage(file="images/right.png")
x_button = Button(image=x_mark, highlightthickness=0, command=generate_word)
x_button.grid(row=2, column=0)
check_mark_button = Button(image=check_mark, highlightthickness=0, command=known_word)
check_mark_button.grid(row=2, column=2)

# labels
language_status = Canvas.create_text(400, 150, text=f" ", font=(FONT, 40, "italic"))
# language_status.grid(row=0, column=1)
word_displayed = Canvas.create_text(400, 263, text=f" ", font=(FONT, 60, "bold"))
# french_word.grid(row=1,column=1)

generate_word()

window.mainloop()

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    fr_2_en_dict = original_data.to_dict(orient="records")
else:
    fr_2_en_dict = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(fr_2_en_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text="{}".format(current_card["French"]), fill="black")
    canvas.itemconfig(card_img, image=front)
    flip_timer = window.after(3000, flip_card)


def right():
    fr_2_en_dict.remove(current_card)
    df = pandas.DataFrame(fr_2_en_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_img, image=back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text="{}".format(current_card["English"]), fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

yes = PhotoImage(file="images/right.png")
right_button = Button(image=yes, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

no = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=no, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()

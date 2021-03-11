from tkinter import *
import pandas as pd
from tkinter import messagebox
import random

df = pd.read_csv('french_words.csv')
current_card = 'French'

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Button Functions ---------------------- #

def get_new_word():
    global df
    global current_card

    if current_card == 'French':
        random_word = df.iloc[random.randint(0,len(df)-1)]
        word = random_word['French']
        translation = random_word['English']
    else:
        random_word = df.iloc[random.randint(0,len(df)-1)]
        word = random_word['English']
        translation = random_word['French']

    canvas.itemconfigure(word_label, text = word)
    canvas.itemconfigure(language_label, text = current_card)

def flip_card():
    global current_card
    canvas.create_image(400, 263, image=back_image)
    if current_card == 'French':
        current_card = 'English'
    else:
        current_card = 'French'
        canvas.itemconfigure(language_label, text=current_card, fill = 'White')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='card_front.png')
back_image = PhotoImage(file = 'card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)  # half the width and height
language_label = canvas.create_text(400, 150, text=current_card, font=('Arial', 40, 'italic'))
word_label = canvas.create_text(400, 250, text='', font=('Arial', '60', 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


def create_button(row, column, columnspan, width, image):
    button = Button(image=image)
    button.config(width=width, pady=5, padx=4)
    button.grid(row=row, column=column, columnspan=columnspan)
    return button

wrong_image = PhotoImage(file='wrong.png')
wrong_button = create_button(row=6, column=0, columnspan=1, width=100, image=wrong_image)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command = get_new_word)

correct_image = PhotoImage(file='right.png')
correct_button = create_button(row=6, column=1, columnspan=1, width=100, image=correct_image)
correct_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command = get_new_word)

get_new_word()


window.mainloop()

from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


class Flashy:
    def __init__(self):
        self.current_card = 'French'
        self.df = pd.read_csv('french_words.csv')
        self.words_chosen = []
        self.correct_words = []

        self.window = Tk()
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.title('Flashy')

        self.front_image = PhotoImage(file='card_front.png')
        self.back_image = PhotoImage(file='card_back.png')
        self.canvas = self.create_canvas()

        self.wrong_image = PhotoImage(file='wrong.png')
        self.correct_image = PhotoImage(file='right.png')
        self.create_buttons()

        self.timer()
        self.loop()

    def create_canvas(self):
        canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

        canvas.create_image(400, 263, image=self.front_image)  # half the width and height
        canvas.create_text(400, 150, text=self.current_card, font=('Arial', 40, 'italic'))
        canvas.create_text(400, 250, text='', font=('Arial', '60', 'bold'))

        canvas.grid(row=0, column=0, columnspan=2)
        return canvas

    def create_button(self, row, column, columnspan, width, image):
        button = Button(image=image)
        button.config(width=width, pady=5, padx=4)
        button.grid(row=row, column=column, columnspan=columnspan)
        return button

    def create_buttons(self):
        wrong_button = self.create_button(row=6, column=0, columnspan=1, width=100, image=self.wrong_image)
        wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=self.flip_card)

        correct_button = self.create_button(row=6, column=1, columnspan=1, width=100, image=self.correct_image)
        correct_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=self.correct_choice)

    def flip_card(self):
        random_word = random_word = self.df.iloc[random.randint(0, len(self.df) - 1)]
        word = random_word['French']
        translation = random_word['English']
        print(len(self.df))

        if self.current_card == 'English':
            self.canvas.create_image(400, 263, image=self.back_image)
            self.language_label = self.canvas.create_text(400, 150, text=self.current_card,
                                                          font=('Arial', 40, 'italic'), fill='White')
            self.canvas.create_text(400, 250, text=self.words_chosen[-1][-1], font=('Arial', '60', 'bold'), fill='White')
            self.current_card = 'French'

        else:
            self.canvas.create_image(400, 263, image=self.front_image)
            language_label = self.canvas.create_text(400, 150, text=self.current_card, font=('Arial', 40, 'italic'),
                                                     fill='Black')
            self.canvas.create_text(400, 250, text=word, font=('Arial', '60', 'bold'), fill='Black')
            self.words_chosen.append([word,translation])
            self.current_card = 'English'

    def correct_choice(self):
        self.flip_card()
        self.correct_words.append(self.words_chosen[-2][0])

        self.df = self.df[~self.df.French.isin(self.correct_words)]
        self.df.to_csv('words_to_learn.csv')

    def timer(self):
        self.window.after(6000, self.timer)
        self.flip_card()

    def loop(self):
        self.window.mainloop()


Flashy()

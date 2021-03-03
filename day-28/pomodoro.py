from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


class Pomodoro:
    def __init__(self):
        self.window = Tk()
        self.window.title('Pomodoro')
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.timer_label = self.create_label(row=0, column=1, text='Timer', size=30)
        self.timer_label.config(fg=GREEN, bg=YELLOW)
        self.work_completed = 0
        self.reps = 0

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file='tomato.png')
        self.canvas.create_image(100, 112, image=self.tomato_img)  # half the width and height
        self.timer_text = self.canvas.create_text(100, 130, text='25:00', fill='white', font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=1)

        self.start = Button(text='Start', highlightthickness=0, command=self.start_timer)
        self.start.grid(row=2, column=0)

        self.checkmark = self.create_label(row=3, column=1, text='', size=12)
        self.checkmark.config(fg=GREEN, bg=YELLOW)

        self.reset = Button(text='Reset', highlightthickness=0, command=self.reset)
        self.reset.grid(row=2, column=2)

        self.window.mainloop()

    def create_label(self, row, column, text, size):
        label = Label(text=text, font=(FONT_NAME, size))
        label.grid(row=row, column=column)
        return label

    def loop(self):
        self.window.mainloop()

    def count_down(self, count):
        minutes, seconds = divmod(count, 60)
        if seconds == 0:
            seconds = '00'
        elif seconds < 10:
            seconds = f'0{seconds}'
        time_formatted = f'{minutes}:{seconds}'
        self.canvas.itemconfig(self.timer_text, text=time_formatted)
        if count > 0:
            self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

    def start_timer(self):
        self.reps += 1
        work_time = 10
        quick_break = 5
        long_break = 20

        if self.reps in [1, 3, 5, 7]:
            self.count_down(work_time)
            self.timer_label.config(text='Timer', fg=GREEN)

        elif self.reps in [2, 4, 6]:
            self.work_completed += 1
            self.checkmark.config(text='✔' * self.work_completed)
            self.count_down(quick_break)
            self.timer_label.config(text='Break', fg=PINK)

        elif self.reps == 8:
            self.work_completed += 1
            self.checkmark.config(text='✔' * self.work_completed)
            self.count_down(long_break)
            self.timer_label.config(text='Break', fg=RED)

    def reset(self):
        self.window.destroy()
        Pomodoro()


Pomodoro()

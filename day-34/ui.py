THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = 0
        self.score_label = self.create_label(row=0, column=1, text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR, fg='white', font=("Arial", 15))

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question = self.canvas.create_text(150, 130,
                                                text="Questions begin here...",
                                                width=250, font=("Arial", 18, "italic"), fill="black")

        self.right_answer_img = PhotoImage(file='true.png')
        self.wrong_answer_img = PhotoImage(file='false.png')

        self.right_button = self.create_button(row=2, column=0, columnspan=1, image=self.right_answer_img)
        self.right_button.config(command = self.true_button)
        self.wrong_button = self.create_button(row=2, column=1, columnspan=1, image=self.wrong_answer_img)
        self.wrong_button.config(command = self.false_button)

        self.generate_question()

        self.window.mainloop()

    def create_button(self, row, column, columnspan, image):
        button = Button(image=image)
        button.grid(row=row, column=column, columnspan=columnspan)
        button.config(highlightthickness=0, pady=100, bg=THEME_COLOR)
        return button

    def create_label(self, row, column, text):
        label = Label(text=text)
        label.grid(row=row, column=column)
        return label

    def generate_question(self):
        self.canvas.config(bg = 'white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text = q_text)

    def true_button(self):
        if self.quiz.question_number < 10:
            check = self.quiz.check_answer('True')
            if check == True:
                self.score +=1
                self.give_feedback(check)
            self.score_label.config(text=f"Score: {self.score}")
            self.give_feedback(check)
        else:
            self.canvas.itemconfig(self.question, text=f'Final score: {self.score}')


    def false_button(self):
        if self.quiz.question_number < 10:
            check = self.quiz.check_answer('False')
            if check == True:
                self.score +=1
            self.score_label.config(text=f"Score: {self.score}")
            self.give_feedback(check)
        else:
            self.canvas.itemconfig(self.question, text=f'Final score: {self.score}')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1500,self.generate_question)

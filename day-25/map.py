from turtle import Turtle, Screen

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.title('U.S States Game')
        self.image = 'blank_states_img.gif'
        self.screen.addshape(self.image)
        self.screen.setup(width = 735, height = 491)
        self.shape(self.image)
        self.score = 0
        self.states_chosen = []
    def user_input(self):
        self.answer = self.screen.textinput(title=f"{self.score} / 50 States Correct", prompt="Whats another state's name?").lower()
        if self.answer != 'quit':
            self.states_chosen.append(self.answer)
        return self.answer
    def update_score(self):
        self.score +=1

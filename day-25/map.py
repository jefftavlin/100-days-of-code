from turtle import Turtle, Screen

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.title('U.S States Game')
        self.image = 'blank_states_img.gif'
        self.screen.addshape(self.image)
        self.shape(self.image)
    def user_input(self):
        self.answer = self.screen.textinput(title="Guess the State", prompt="Whats another state's name?").lower()
        return self.answer
    def place_state(self):
        pass

from turtle import Screen, Turtle
import pandas as pd
from map import Map
from map_game import Game

df = pd.read_csv('50_states.csv')
df['state'] = df['state'].apply(lambda x: x.lower())

map = Map()

game = True
while game:
    answer_state = map.user_input()
    if answer_state in df['state'].values:
        state = Game(df, answer_state)
    else:
        pass

map.screen.exitonclick()

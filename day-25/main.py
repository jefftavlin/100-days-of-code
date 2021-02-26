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
        map.update_score()
        state = Game(df, answer_state)
    elif answer_state == 'quit':
        break
    else:
        pass

map.screen.exitonclick()

missing_states = df[~df['state'].isin(map.states_chosen)]
missing_states['state'].to_csv('wrong_answer.csv')

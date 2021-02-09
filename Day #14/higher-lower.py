from art import logo, vs
from game_data import data
import random
from replit import clear

score = 0
length = len(data) - 1

def more_followers(a,b):
  a = a['follower_count']
  b = b['follower_count']
  if a > b:
    return 'A'
  else:
    return 'B'

def display_text(a,b, score):
  if score == 0:
    print(logo)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against b: {b['name']}, {b['description']}, from {b['country']}.")
  else:
    print(logo)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against b: {b['name']}, {b['description']}, from {b['country']}.")


while True:
  if score == 0:
    choice_a = data.pop(random.randint(0,length))
    choice_b = data.pop(random.randint(0,length))
  else:
    choice_a = choice_b
    choice_b = data.pop(random.randint(0,length))

  display_text(choice_a,choice_b, score)

  answer = input("Who has more followers? Type 'A' or 'B': ").title()
  correct = more_followers(choice_a, choice_b)

  clear()

  if answer == correct:
    score +=1
  else:
    break

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")

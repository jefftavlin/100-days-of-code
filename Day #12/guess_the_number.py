#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random


logo = """
   ____                       _____ _            _   _                 _               
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                 
"""

def correct_guess(guess, number):
  if guess > number:
    print('Too high.')
  elif guess < number:
    print('Too low.')
  else:
    print(f"You win! The right number was {number}")
    return True

def lives_left(lives):
  print(f"You have {lives} attemps remaining to guess the number.")



number = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == 'easy':
    lives = 10
    break
  elif level == 'hard':
    lives = 5
    break
  else:
    print("Please either type 'easy' or 'hard'")

while lives > 0:
  lives_left(lives)
  guess = int(input('Make a guess: '))
  correct_guess(guess, number)
  if guess == number:
    break
  lives -=1
 
if guess != number:
  print(f"You've run out of guesses you lose. The correct number was {number}")

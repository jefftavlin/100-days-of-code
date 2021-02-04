#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_' for c in chosen_word]
correct = None
lives = 6

while '_' in display:
  guess = input("Guess a letter: ").lower()
  #Check guessed letter
  for i,letter in enumerate(chosen_word):
    if letter == guess:
      display[i] = letter
      correct = True

  if correct != True:
    print(stages[lives])
    lives -= 1

  print(f"{' '.join(display)}")

  if lives < 0 :
    break

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

  #Join all the elements in the list and turn it into a String.

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining

#Check if user has got all letters.
if "_" not in display:
  print("You win.")
else:
  print('You lose.')

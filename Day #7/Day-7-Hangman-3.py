#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_' for c in chosen_word]

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while '_' in display:
  guess = input("Guess a letter: ").lower()
  #Check guessed letter
  for i,letter in enumerate(chosen_word):
      if letter == guess:
          display[i] = letter
          print("Right")
      else:
          print("Wrong")
  print(display)
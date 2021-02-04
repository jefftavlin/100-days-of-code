import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_' for c in chosen_word]
correct = None
guessed = []

while '_' in display:
  guess = input("Guess a letter: ").lower()
  guessed.append(guess)
  correct = False

  if guessed.count(guess) >= 2:
    print(f'You have already guessed {guess} before\n')

  else:
    if guess in chosen_word:
      #Check guessed letter
      for i, letter in enumerate(chosen_word):
        if letter == guess:
          display[i] = letter
          correct = True

    if correct != True:
      print(f'The letter {guess} is not in the word.')
      print(stages[lives])
      lives -= 1

    print(f"{' '.join(display)}")

    if lives < 0 :
      break

if "_" not in display:
  print("You win.")
else:
  print('You lose.')

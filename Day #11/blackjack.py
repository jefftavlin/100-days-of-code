############### Blackjack Project #####################
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score = 0
computer_score = 0

def starter_hand():
  hand = random.choices(cards, k = 2)
  return hand

def calculate_score(hand):
  score = sum(hand)
  if score > 21:
    if 11 in hand:
      hand[hand.index(11)] = 1
      score = sum(hand)
  return score

def display_score(player, player_score, computer):
  print(f" Your cards {player}, current score: {player_score}")
  print(f" Computer's first card: {computer[0]}")

def winner(player, computer):
  player_score = sum(player)
  computer_score = sum(computer)

  if player_score > 21:
    print('You went over. You lose!')
  elif player_score == computer_score:
    print('Tie.')
  elif computer_score > 21:
    print("Dealer went over. You win!")
  elif player_score > computer_score:
    print("You win!")
  elif computer_score < player_score:
    print('You lose!')

while True:
  print(logo)
  starter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if starter == 'n':
    clear()
    break
  elif starter != 'y':
    print("Please either type 'y' or 'n'.")
    continue
  else:
    player_hand = starter_hand()
    computer_hand = starter_hand()

    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    display_score(player_hand, player_score, computer_hand)

    while True:
      if calculate_score(player_hand) == 21 or calculate_score(computer_hand) == 21:
        if calculate_score(player_hand) == 21 and calculate_score(computer_hand) != 21:
          print('You win!')
        else:
          print('Computer wins.')
        break
      else:
        if calculate_score(player_hand) < 21:
          y_n = input("Type 'y' to get another card, type 'n' to pass: ")
          if y_n == 'n':
            while calculate_score(computer_hand) < 16:
              computer_hand.append(random.choice(cards))
            break
          elif y_n == 'y':
            player_hand.append(random.choice(cards))
            display_score(player_hand, calculate_score(player_hand), computer_hand)
        else:
          break

    print(f"Your final hand: {player_hand}, your score: {calculate_score(player_hand)}")
    print(f"Computer's final hand: {computer_hand}, score: {calculate_score(computer_hand)}")

    winner(player_hand, computer_hand)
    
    play_again = input("Would you like to play again? Type 'y' or 'n'")
    if play_again == 'n':
      break
    else:
      clear()

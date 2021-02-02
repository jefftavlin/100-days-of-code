rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

valid_options = [0,1,2]
images = [rock,paper,scissors]

while True:
    player_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
    try:
      if int(player_choice) in valid_options:
        break
    except ValueError:
      continue
player_choice = int(player_choice)
computer_choice = random.randint(0,2)
print(images[int(player_choice)])

print(f'Computer chose: {computer_choice}\n')
print(images[int(computer_choice)])

if player_choice == 0 and computer_choice == 2:
  print('You win.')
elif player_choice == computer_choice:
  print('Tie.')
elif player_choice == 1 and computer_choice == 0:
  print('You win.')
elif player_choice == 2 and computer_choice == 1:
  print('You win.')
else:
  print('You lose.')

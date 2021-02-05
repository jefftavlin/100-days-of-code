from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
bidders = {}

def add_values(name, bid):
  bidders[name] = bid

def highest_bidder(dictionary):
    names = [key for key in dictionary]
    bids = [value for value in dictionary.values()]
    winner = names[bids.index(max(bids))]
    return winner

print(logo)
print("Welcome to the secret auction program.")

while True:
  name = input('What is your name?: ').title()
  bid = int(input("What's your bid?: $"))
  add_values(name, bid)
  yes_no = input("Are there any other bidders?: Type 'yes' or 'no'.\n")
  clear()
  if yes_no == 'no':
    winner = highest_bidder(bidders)
    print(f'The winner of the bid is {winner}.')
    break

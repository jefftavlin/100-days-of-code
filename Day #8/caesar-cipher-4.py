from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  shifted = []
  for letter in text:
    if direction == 'encode':
      shifted.append(alphabet[alphabet.index(letter) + shift])
    elif direction == 'decode':
      shifted.append(alphabet[alphabet.index(letter) - shift])
    else:
      shifted.append(letter)
  print(''.join(shifted))

print(logo)

while True:
  while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
      break
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  question = input('\nWould you like to go again? (y/n) \n').lower()
  if question == 'n':
    break

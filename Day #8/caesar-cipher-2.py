alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  shifted = []
  for letter in text:
    if letter.isalpha() == True:
      shifted.append(chr(ord(letter) + shift))
    else:
      shifted.append(letter)
  print(''.join(shifted))

def decrypt(text, shift):
  shifted = []
  for letter in text:
    if letter.isalpha() == True:
      shifted.append(chr(ord(letter) - shift))
    else:
      shifted.append(letter)
  print(''.join(shifted))

if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)

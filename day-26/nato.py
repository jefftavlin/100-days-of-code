import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input('Enter a word: ').upper()
result = [nato[c] for c in name]
print(result)

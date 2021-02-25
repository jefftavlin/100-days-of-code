#TODO: Create a letter using starting_letter.txt

name_path ='C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Input/Names/invited_names.txt'
starting_letter_path = 'C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt'
output_path = 'C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Output'

with open(name_path) as names:
    names = names.readlines()

with open(starting_letter_path) as starting_letter:
    starting_letter = starting_letter.readlines()

names = [name.split('\n')[0] for name in names]

def replace_name(letter_to_use, name):
    final_letter = []
    for line in letter_to_use:
        if '[name]' in line:
            final_letter.append(f'Dear {name}, \n')
        else:
            final_letter.append(line)
    return final_letter

def create_file_paths(name):
    final_path = f'{output_path}/letter_for_{name}.txt'
    return final_path

for name in names:
    file_path = create_file_paths(name)
    letter = replace_name(starting_letter, name)
    with open(file_path, 'w') as file:
        for line in letter:
            file.write(line)

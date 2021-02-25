#TODO: Create a letter using starting_letter.txt

name_path ='C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Input/Names/invited_names.txt'
starting_letter_path = 'C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt'
output_path = 'C:/Users/Jeff/Documents/Python/100 Days of Code/day-24/Mail Merge Project Start/Output'

with open(name_path) as names:
    names = names.readlines()

with open(starting_letter_path) as starting_letter:
    starting_letter = starting_letter.readlines()

names = [name.split('\n')[0] for name in names]

class Letter():
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

        self.final_letter = self.replace_name()
        self.final_path = self.create_file_paths()

    def replace_name(self):
        final_letter = []
        for line in self.letter:
            if '[name]' in line:
                final_letter.append(f'Dear {self.name}, \n')
            else:
                final_letter.append(line)
        return final_letter

    def create_file_paths(self):
        final_path = f'{output_path}/letter_for_{self.name}.txt'
        return final_path


for name in names:
    current_letter = Letter(name, starting_letter)
    with open(current_letter.final_path, 'w') as file:
        for line in current_letter.final_letter:
            file.write(line)

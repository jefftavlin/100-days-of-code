from tkinter import *
import pandas as pd
from tkinter import messagebox
import random
df = pd.read_csv('passwords.csv')

# ---------------------------- SEARCH ------------------------------------------ #
def search():
    global df
    website = website_entry.get().title()
    searched = df[df['website'] == website]
    if len(website) == 0:
        messagebox.showerror(title ='N/A',
                             message= 'Please enter a valid website.')
    elif len(searched) == 0:
        messagebox.showinfo(title=website,
                            message = f'No password saved for {website}.')
    else:
        messagebox.showinfo(title = website,
                            message = f'Email: {searched["email"].values[0]}'
                                      f'\nPassword: {searched["password"].values[0]}')
        email_entry.delete(0, END)
        password_entry.delete(0, END)

        email_entry.insert(0, searched["email"].values[0])
        password_entry.insert(0, searched["password"].values[0])


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password = []

    for i in range(6):
        password.append(random.choice(letters))

    for i in range(2):
        password.append(random.choice(numbers))
        password.append(random.choice(symbols))

    password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def collect_entries():
    global df
    d = {'website':[website_entry.get().title()],
         'email':[email_entry.get()],
         'password':[password_entry.get()]}

    is_ok = messagebox.askokcancel(title = website_entry.get(),
                           message= f'These are the details entered: '
                                    f'\nEmail: {email_entry.get()}'
                                    f'\nPassword: {password_entry.get()}'
                                    f'\nIs it okay to save?')

    if is_ok == True:
        temp_df = pd.DataFrame(data = d)
        df = df.append(temp_df)
        df.to_csv('passwords.csv')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx = 30, pady = 40)
window.title('Password Manager')

canvas = Canvas(width = 200, height = 200)
lock_img = PhotoImage(file = 'logo.png')
canvas.create_image(100, 94, image=lock_img)  # half the width and height
canvas.grid(row = 0, column = 1)

def create_label(row, column, text):
    label = Label(text=text)
    label.grid(row=row, column=column)
    return label

website_label = create_label(row = 1, column = 0, text = 'Website:')
email_label = create_label(row = 2, column = 0, text = 'Email/Username:')
password_label = create_label(row = 3, column = 0, text = 'Password:')

def create_entry(row, column, columnspan, width):
    entry = Entry()
    entry.grid(row= row, column = column, columnspan = columnspan)
    entry.config(width = width)
    return entry

website_entry = create_entry(row = 1, column = 1, columnspan =1, width = 33)
website_entry.focus()
email_entry = create_entry(row = 2, column = 1, columnspan = 3, width = 49)
password_entry = create_entry(row = 3, column = 1, columnspan = 1, width = 33)

def create_button(row, column, columnspan, width, text):
    button = Button(text = text)
    button.config(width = width, pady = 5, padx = 4)
    button.grid(row = row, column = column, columnspan = columnspan)
    return button

add_button = create_button(row=4, column=1,
              columnspan=2, width=42, text="Add")

add_button.config(command = collect_entries)

generate_button = create_button(row = 3, column = 2,
                                columnspan= 1 , width = 12,
                                text = 'Generate Password')

generate_button.config(font = ('Arial',7), command = password_generator)

search_button = create_button(row = 1, column = 2,
                              columnspan= 1, width= 12,
                              text = 'Search')

search_button.config(font = ('Arial', 7), command = search)

window.mainloop()

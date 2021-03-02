import tkinter as tk

def create_label(row, col, text):
    label = tk.Label(text = text, font = ('Arial', 12))
    label.grid(row = row, column = col)
    return label

def calculate():
    miles = float(input.get())
    km = miles * 1.60934
    label_2.config(text = km)

window = tk.Tk()
window.title('Mile to Km Converter')
window.config(padx=25, pady=25)
window.minsize(width=200, height=150)

input = tk.Entry()
input.grid(row = 0, column = 1)

label_1 = create_label(1, 0, "is equal to")
label_2 = create_label(1,1, "0")
label_3 = create_label(0,2, "Miles")
label_4 = create_label(1,2, "Km")

button = tk.Button(text = 'Calculate', command = calculate)
button.grid(row = 2, column = 1)

window.mainloop()

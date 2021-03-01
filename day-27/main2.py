import tkinter

def button_clicked():
    print('I got clicked.')
    if len(input.get()) > 0:
        my_label.config(text = input.get())

window = tkinter.Tk()
window.title('My first gui program')
window.minsize(width=500, height=300)
window.config(padx = 20, pady= 20)

# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, "bold"))
# my_label.place(x = 100, y = 100) # places it on the screen, centered
my_label.grid(column =0, row = 0)

# button
button = tkinter.Button(text = 'click me', command = button_clicked)
button.grid(column = 1, row = 1)

new_button = tkinter.Button(text = 'new', command = button_clicked)
new_button.grid(column = 2, row = 0)

#Entry
input = tkinter.Entry(width = 10)
input.grid(column = 3, row = 2)

window.mainloop()  # end of the program

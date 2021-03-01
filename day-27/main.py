import tkinter

window = tkinter.Tk()
window.title('My first gui program')
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, "bold"))
my_label.pack()  # places it on the screen, centered

# button
def button_clicked():
    print('I got clicked.')
    if len(input.get()) > 0:
        my_label.config(text = input.get())

button = tkinter.Button(text = 'click me', command = button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width = 10)
input.pack()

window.mainloop()  # end of the program

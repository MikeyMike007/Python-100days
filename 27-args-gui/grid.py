import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("'Arial", 24, "bold"))

# Before the label will appear in the window, you need to pack it.
# Pack has a lot of options to it
# my_label.pack()  # pack with no options
my_label.grid(column=0, row=0)

# Change text from initial text
my_label["text"] = "New text"
# Another way to change text
my_label.config(text="Another new text")

clicked = 0


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=3, row=1)

# Entry

input = tkinter.Entry(width=10)
input.grid(column=2, row=2)


window.mainloop()

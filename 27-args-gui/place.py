import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("'Arial", 24, "bold"))

# Before the label will appear in the window, you need to pack it.
# Pack has a lot of options to it
# my_label.pack()  # pack with no options
my_label.place(x=100, y=200)  # pack with text on the side

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
button.place(x=300, y=50)

# Entry

input = tkinter.Entry(width=10)
input.place(x=400, y=400)


window.mainloop()

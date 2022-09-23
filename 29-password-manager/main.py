import tkinter as tk
from tkinter import messagebox
import os
import random
import string
import pyperclip

from PIL import ImageTk, Image

FILE = "my_file.txt"

# ---------------------------- PASSWORD GENERATOR -----------------------


def generate_password():
    length = 13
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    random.seed = os.urandom(1024)

    password = "".join(random.choice(chars) for i in range(length))
    entry_usr_passwd.insert(0, password)
    pyperclip.copy(password)


# Use pyperclip to copy to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    save = (entry_website.get(), entry_usr_name.get(), entry_usr_passwd.get())
    text_to_save = " | ".join(save)
    text_to_save += "\n"

    if len(save[0]) == 0 or len(save[1]) == 0 or len(save[2]) == 0:
        messagebox.showerror(
            title="Opps", message="Please make sure that all fields are empty"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=save[0],
            message=f"These are the details you entered:\n \
            Email: {save[1]}\n \
            Password: {save[2]}\n \
            Is it ok to save?\n Is it ok to save?",
        )

        if is_ok:
            with open(FILE, mode="a") as file:
                file.write(text_to_save)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password manager")
window.configure(width=400, height=400, padx=20, pady=20)


canvas = tk.Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

img = ImageTk.PhotoImage(Image.open("logo.png"))
canvas.create_image(100, 100, image=img)


lbl_website = tk.Label(text="Website:")
lbl_usr_name = tk.Label(text="Email / Username:")
lbl_usr_passwd = tk.Label(text="Password:")

lbl_website.grid(row=1, column=0)
lbl_usr_name.grid(row=2, column=0)
lbl_usr_passwd.grid(row=3, column=0)

entry_website = tk.Entry(width=35)
entry_usr_name = tk.Entry(width=35)
entry_usr_passwd = tk.Entry(width=21)

entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_usr_name.grid(row=2, column=1, columnspan=2)
entry_usr_name.insert(0, "angela@gmail.com")
entry_usr_passwd.grid(row=3, column=1)

btn_gen_passwd = tk.Button(
    text="Generate password", width=35 - 21, command=generate_password
)
btn_gen_passwd.grid(row=3, column=2)

btn_add = tk.Button(text="Add", width=35, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)


window.mainloop()

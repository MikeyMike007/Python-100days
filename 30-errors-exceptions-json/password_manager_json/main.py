import tkinter as tk
from tkinter import messagebox
import os
import random
import string
import pyperclip
import json

from PIL import ImageTk, Image

FILE = "data.json"

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
    website = entry_website.get()
    email = entry_usr_name.get()
    password = entry_usr_passwd.get()

    new_data = {
        website: {"email": email, "password": password},
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Opps", message="Please make sure that all fields are empty"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details you entered:\n \
            Email: {email}\n \
            Password: {password}\n \
            Is it ok to save?\n Is it ok to save?",
        )

        if is_ok:
            try:
                with open(FILE, "r") as file:
                    # Read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open(FILE, "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Update old data with new data
                data.update(new_data)
                with open(FILE, "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, tk.END)
                entry_usr_passwd.delete(0, tk.END)


# ---------------------------- SEARCH PASSWORD -------------------------#
def search():
    website = entry_website.get()
    email = entry_usr_name.get()
    password = ""

    if len(website) == 0 or len(email) == 0:
        messagebox.showerror("Please provide a website and a username")
    else:
        try:
            with open(FILE, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=website,
                    message=f"Email: {email}\nPassword: {password}",
                )
            else:
                messagebox.showinfo(
                    title="Error",
                    message=f"You dont have password saved for {website}",
                )


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

entry_website = tk.Entry(width=30)
entry_usr_name = tk.Entry(width=50)
entry_usr_passwd = tk.Entry(width=30)

entry_website.grid(row=1, column=1)
entry_website.focus()
entry_usr_name.grid(row=2, column=1, columnspan=2)
entry_usr_name.insert(0, "angela@gmail.com")
entry_usr_passwd.grid(row=3, column=1)

btn_gen_passwd = tk.Button(
    text="Generate password", command=generate_password, width=15
)

btn_search = tk.Button(text="Search", command=search, width=15)
btn_gen_passwd.grid(row=3, column=2)
btn_search.grid(row=1, column=2)

btn_add = tk.Button(text="Add", command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)


window.mainloop()

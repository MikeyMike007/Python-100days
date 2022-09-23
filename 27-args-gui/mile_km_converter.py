import tkinter as tk

# Window
# -------------------------

# Creating a new window and configurations
window = tk.Tk()
window.title("Widget examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


# Entries
# -------------------------
entry = tk.Entry(width=30)
entry.insert(tk.END, string="0")
print(entry.get())

entry.grid(row=0, column=1)


# Labels
# -------------------------
texts = ["Miles", "is equal to", "Km"]
coordinates = [(0, 2), (1, 0), (1, 2)]
text_coordinates = list(zip(texts, coordinates))
labels = []

for text, coordinates in text_coordinates:
    label = tk.Label(text=text)
    label.grid(row=coordinates[0], column=coordinates[1])
    labels.append(label)


# Label Result
# -------------------------
result = tk.Label(text="0")
result.grid(row=1, column=1)


def action():
    miles = float(entry.get())
    km = miles * 1.6
    result.config(text=f"{str(km)}")


# Calls function action() when clicked
button = tk.Button(text="Calculate", command=action)
button.grid(row=2, column=1)


window.mainloop()

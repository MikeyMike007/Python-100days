# Following program displays Kanye quotes in a GUI app
import tkinter as tk
import requests


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Kanye Says...")
        self.config(padx=50, pady=50)

        self.background_img = tk.PhotoImage(file="background.png")
        self.canvas = tk.Canvas(width=300, height=414)
        self.canvas.create_image(150, 207, image=self.background_img)
        self.get_quote()

        self.quote_text = self.canvas.create_text(
            150,
            207,
            text=self.quote,
            width=250,
            font=("Arial", 18, "bold"),
            fill="white",
        )
        self.canvas.grid(row=0, column=0)

        self.kanye_img = tk.PhotoImage(file="kanye.png")
        self.kanye_button = tk.Button(
            image=self.kanye_img, highlightthickness=0, command=self.get_update_quote
        )
        self.kanye_button.grid(row=1, column=0)

    def get_quote(self):
        response = requests.get(url="https://api.kanye.rest")
        current_quote = response.json()["quote"]
        self.quote = current_quote

    def update_gui_quote(self):
        self.canvas.itemconfigure(self.quote_text, text=self.quote)

    def get_update_quote(self):
        self.get_quote()
        self.update_gui_quote()


if __name__ == "__main__":
    app = App()
    app.mainloop()

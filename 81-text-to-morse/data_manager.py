import requests
from bs4 import BeautifulSoup
import pandas as pd


class DataManager:
    def __init__(self):
        self.morse_library = {}

    def read_data_web(self):
        # A site i found
        url = "http://www.sckans.edu/~sireland/radio/code.html"
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all(name="table")

        for table in tables:
            for row in table.find_all(name="tr"):
                cells = row.find_all(name="td")
                if len(cells) != 0:
                    char = cells[0].text.lower().strip()
                    morse = cells[1].text.lower().strip().replace("*", ".")
                    self.morse_library[char] = morse

    def print_library(self):
        for char, morse in self.morse_library.items():
            print(f"Char: {char} - Morse: {morse}")

    def to_csv(self):
        df = pd.DataFrame(self.morse_library.items(), columns=["char", "morse"])
        df.to_csv("morse.csv")

    def read_data_csv(self, csv_file):
        with open(csv_file) as file:
            for data in file.readlines()[1:]:  # First line is header
                char = data.split(",")[1].strip()
                morse = data.split(",")[2].strip()
                self.morse_library[char] = morse

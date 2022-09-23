import pandas as pd

data: pd.DataFrame = pd.read_csv("./nato_phonetic_alphabet.csv")

# TODO: Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

# TODO: Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
nato_list = [nato_dict[letter] for letter in word.upper()]
print(nato_list)

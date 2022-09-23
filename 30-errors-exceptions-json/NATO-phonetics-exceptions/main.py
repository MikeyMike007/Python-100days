import pandas as pd

data: pd.DataFrame = pd.read_csv("./nato_phonetic_alphabet.csv")

# TODO: Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetics():
    # TODO: Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ")

    try:
        nato_list = [nato_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Only characters is allowed as input")
        generate_phonetics()
    else:
        print(nato_list)


generate_phonetics()

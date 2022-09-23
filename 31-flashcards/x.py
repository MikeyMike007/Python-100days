import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# Data
# ----------------------
try:
    df: pd.DataFrame = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df: pd.DataFrame = pd.read_csv("./data/french_words.csv")
else:
    pass
data = df.to_dict(orient="records")

print(data)

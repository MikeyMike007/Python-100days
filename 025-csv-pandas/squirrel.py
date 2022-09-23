import pandas as pd

data = pd.read_csv(
    "./squirells.csv",
)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)


red_squirrels_count = len(data[data["Primary Fur Color"] == "Red"])
print(red_squirrels_count)


black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("./squirrel_count.csv")

import pandas as pd

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Loop through a dictionary
for (key, value) in student_dict.items():
    print(f"key: {key} - value: {value}")

# Loop through a dataframe - Not optimal
student_dataframe = pd.DataFrame(student_dict)
for (key, value) in student_dataframe.items():
    print(f"key: {key} - value: {value}")

# Better looping with Pandas using iterrows
for (index, row) in student_dataframe.iterrows():
    print(index)

for (index, row) in student_dataframe.iterrows():
    print(row)

for (index, row) in student_dataframe.iterrows():
    print(f"row.student: {row.student} - row.score: {row.score}")


for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)

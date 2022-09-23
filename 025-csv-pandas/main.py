import pandas

# Pandas is the best choice to manage tabular data

# Pandas have two important objects - DataFrame and Series
data: pandas.DataFrame = pandas.read_csv("./weather_data.csv")
temperatures: pandas.Series = data["temp"]


# Convert DataFrame to Dictionary
print("Convert pandas.DataFrame to Dictionary")
data_dict = data.to_dict()
print(data_dict)


# Convert pandas.Series to List
print("Convert pandas.Series to List")
temp_list = temperatures.to_list()
print(temp_list)

# Use pandas to calculate average temp
print("Use pandas to calculate average temp")
avg_temp = temperatures.mean()
print(f"Average temperature: {avg_temp}")


# Use pandas to calculate max temp
print("Use pandas to calculate max temp")
max_temp = temperatures.max()
print(f"Max temp: {max_temp}")

# Alternative way of extracting Series from a DataFrame
# Pandas creates pandas.Series objects with the same name as the headers
print("Alternative way of extracting Series from a DataFrame")
print(data.day)
print(data.temp)
print(data.condition)

print("Illustrations on getting row data")

# Print rows where day is Monday
print("Print rows where day is Monday")
print(data[data["day"] == "Monday"])

# Print out the row with max temp
print("Print out the row with the max temp")
print(data[data["temp"] == data["temp"].max()])


# Save rows where day is Monday
print("Save rows where day is Monday")
mondays = data[data["day"] == "Monday"]
print("Condition on Mondays are:")
print(mondays["condition"])

# Get temperatures on Mondays
monday_temps = mondays["temp"]
farenheit_temps = monday_temps * 9 / 5 + 32
print("Monday temperatures in Farenheit")
print(farenheit_temps)

# Create a DataFrame
print("Create a Dataframe")
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
df = pandas.DataFrame(data_dict)
print(df)
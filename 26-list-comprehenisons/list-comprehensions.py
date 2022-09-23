# Compare following two code snippets to see how much clear it is to write list
# comprehensions

# With foe loop
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# With list-comprehension

new_list_comp = [n + 1 for n in numbers]

print(new_list)  # [2,3,4]
print(new_list_comp)  # [2,3,4]

# Another example - Create a list of characters in a name
name = "Angela"
letters = [letter for letter in name]
print(letters)  # ['A', 'n', 'g',...]

# Challenge - Double numbers in a range
range_list = [x * 2 for x in range(1, 6)]

# Conditional list comprehension
a = [1, 2, 4, 6, 44, 10]
b = [1, 5, 7, 44, 11]

intersection = [number for number in a if number in b]
numbers_unique_to_a = [number for number in a if number not in b]
numbers_unique_to_b = [number for number in b if number not in a]

print(intersection)
print(numbers_unique_to_a)
print(numbers_unique_to_b)

# Take out names with less than 5 characters
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name for name in names if len(name) > 4]
print(short_names)
print(long_names)

# Interactive coding exercice 1
# ---------------------------------
# Square the numbers in list numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Interactive coding exercise 2
# ---------------------------------------
# Take a look inside file1.txt and file2.txt. They each contain a bunch of
# numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that
# are common in both files

file1_numbers = []
file2_numbers = []

with open("./file1.txt") as file1:
    for row in file1.readlines():
        number = int(row.rstrip())
        file1_numbers.append(number)


with open("./file2.txt") as file2:
    for row in file2.readlines():
        number = int(row.rstrip())
        file2_numbers.append(number)

numbers_both_in_f1_f2 = [number for number in file1_numbers if number in file2_numbers]
print(numbers_both_in_f1_f2)

# Another great answer to the same interactive coding exercise
#
# def filereader(file):
#   """Read file and remove newline tag"""
#   with open(file, "r") as file:
#     f_read = file.readlines()
#     f = [int(i.replace("\n", "")) for i in f_read]
#     return f
#
# file1 = filereader("file1.txt")
# file2 = filereader("file2.txt")
#
# # find duplicates and save to result
# result = [num for num in file1 if num in file2]
#
#
# print(result)

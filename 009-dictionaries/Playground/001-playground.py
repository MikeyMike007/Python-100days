programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

#Adding items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and ovber again"


#Edit an item in a dictionary

programming_dictionary["Bug"] = "Edited bug"


#Loop though a dictionary - it will only give you the keys
for item in programming_dictionary:
    print(item)

for key in programming_dictionary:
    # prints the key
    print(key)
    # prints the value
    print(programming_dictionary[key])

#Prints key and value direclty
for key, value in programming_dictionary.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


#Prints (key, value) as a tuple
for key_value_tup in programming_dictionary.items():
   print(key_value_tup)

# Create an empty dictionary
empty_dict = {}

#Wipe and existing dictionary
programming_dictionary = {}


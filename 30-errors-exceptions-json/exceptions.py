# File not found error
# Following code crashes if the file "a_file.txt" doesnt exist
# with open("a_file.txt") as file:
#     file.read()  # Error

# Key Error
# a_dict = {"key": "value"}
# a_value = a_dict["non_existent_key"]  # Error

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[4]  # Error

# Type Error
# text = "abc"
# print(text + 5)  # Error


# You can manage these crahses though exceptions with keywords
# - try: - Something that might cause an exception
# - except: - Do this if there is an exception
# - else: - Do this if there were no exceptions
# - finally: - Do this no matter what happends
# - raise: Raise you own Error

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["nonexistent_key"])

except FileNotFoundError:
    print("File doesnt exist - Creating file")
    file = open("a_file", "w")
    file.write("Hello")

except KeyError as error_message:
    print(f"The key {error_message} doesn not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()

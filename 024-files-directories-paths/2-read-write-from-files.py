# Open file in write mode
# Another write mode is 'a' which means 'append'
with open("my_textfile.txt", "w") as file:
    file.write("Hello, World!")

# Open file in read mode and print the contents of the file
with open("my_textfile.txt") as file:
    contents = file.read()
    print(contents)

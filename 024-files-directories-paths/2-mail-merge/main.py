# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


names = []
placeholder = "[name]"

# Paths to files
invited_names = "./Input/Names/invited_names.txt"
starting_letter = "./Input/Letters/starting_letter.txt"
invitation_letter = "./Output/ReadyToSend/invitation"

with open(invited_names) as file:
    for name in file.readlines():
        names.append(name.rstrip())

with open(starting_letter) as file:
    letter_template = file.read()

for name in names:
    letter_with_name = letter_template.replace(placeholder, name)
    with open(f"{invitation_letter}_{name}.txt", "w") as file:
        file.write(letter_with_name)

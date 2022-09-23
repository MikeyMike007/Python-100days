def formatName(fName, lName):
    if fName == "" or lName ="":
        return #its like break in a function
    formatFName = fName.title()
    formatlName = lName.title()
    return f"{formatFName} {formatlName}"

print(formatName("Mikael","Hatanoää"))
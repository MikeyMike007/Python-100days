# Functions with outputs

Example

```python
def formatName(fName, lName):
    if fName == "" or lName ="":
        return #its like break in a function
    formatFName = fName.title()
    formatlName = lName.title()
    return f"{formatFName} {formatlName}"

print(formatName("Firstname","Surname"))
```

## Docstrings

Example

```python
def myFunc(myVar):
    """Take my variable and add 1 to it"""
    return myVar + 1

myFunc(1)
```


# Python loops

## Using the for loop with python lists

An example of a for loop

```python
fruits = ["banana","pear","apple","mango"]
for fruit in fruits:
    print(f"{fruit} is soo good")
    print(f"{fruit}" + "pie")
```

## Split function

`split: (sep: str | None = …, maxsplit: int = …) -> List[str]`

Return a list of the words in the string, using sep as the delimiter string.

Set the delimiter according which to split the string. None (the default value) means split according to any whitespace, and discard empty strings from the result. maxsplit Maximum number of splits to do. -1 (the default value) means no limit.

Please note that it returns a list.

## For loops and the range function

```python
for x in range(1, 10, 1):
    print(x)
```

Prints:
1
2
3
4
5
6
7
8
9

**Please note that it doesn’t include 10**
**Please also note that you can specify the step size in the third argument**

Calculate all and add all numbers from 1 to 100:

```python
totalNumber = 0
for number in range(1,100 + 1):
    totalNumber += number

print(f"total : {totalNumber}")
```


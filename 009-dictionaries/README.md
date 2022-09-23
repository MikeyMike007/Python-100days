# Day 9 - Dictionaries, nesting and secret auctions

## Dictionaries

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and ovber again"


# Edit an item in a dictionary
programming_dictionary["Bug"] = "Edited bug"


# Loop though a dictionary - it will only give you the keys
for item in programming_dictionary:
    print(item)

for key in programming_dictionary:
    # prints the key
    print(key)
    # prints the value
    print(programming_dictionary[key])

# Prints key and value direclty
for key, value in programming_dictionary.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


# Prints (key, value) as a tuple
for key_value_tup in programming_dictionary.items():
   print(key_value_tup)

# Create an empty dictionary
empty_dict = {}

# Wipe and existing dictionary
programming_dictionary = {}
```

## Nesting lists and dictionaries

Nesting - following is allowed

`{Key: Value}`

`{Key: Value, Key2: Value2,}`

`{Key: [List], Key2: {Dict}}`

`[{Key: [List], Key2: {Dict}}, {Key: Value, Key2: Value2}]`

Example

```python
# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log1 = {
 "France": ["Paris", "Lille", "Dijon"],
 "Germany": ["Berlin", "Hamburg", "Stuttgard"]
}

print(travel_log1["France"][0]) # prints Paris
print(travel_log1["France"][1]) # Prints Lille
print(travel_log1["France"][2]) # prints Dijon

# Nesting a list in a dictionary
travel_log2 = {
 "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
 "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"] , "total_visits": 5},
}

print(travel_log2["France"]) # prints {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
print(travel_log2["France"]["cities_visited"]) # prints ["Paris", "Lille", "Dijon"]
print(travel_log2["France"]["cities_visited"][0]) # prints Paris
print(travel_log2["France"]["cities_visited"][1]) # prints Lille
print(travel_log2["France"]["cities_visited"][2]) # prints Dijon
print(travel_log2["France"]["total_visits"]) # prints 12

# Nesting a dictionary in a dictionary
cities_visited = {
 "France": {
    "Paris": 5,
    "Lille": 10,
    "Dijon": 15
    },

 "Germany": {
    "Berlin": 5,
    "Hamburg": 10,
    "Stuttgart": 15
    }
 }

print(cities_visited["France"]) # prints {'Paris': 5, 'Lille': 10, 'Dijon': 15}
print(cities_visited["France"]["Paris"]) # print 5

# Nesting dictionary in a list
travel_log3 = [
    {
        "Country": "France",
        "Cities_vitied": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12

    },
    {
        "Country": "Germany",
        "Cities_vitied": ["Berlin", "hamburg", "Stuttgart"],
        "Total_visits": 12

    }
]

print(travel_log3)
```


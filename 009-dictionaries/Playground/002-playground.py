#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary
travel_log1 = {
 "France": ["Paris", "Lille", "Dijon"],
 "Germany": ["Berlin", "Hamburg", "Stuttgard"]   
}

print(travel_log1["France"][0]) # prints Paris
print(travel_log1["France"][1]) # Prints Lille
print(travel_log1["France"][2]) # prints Dijon

#Nesting a list in a dictionary
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

#Nesting a dictionary in a dictionary
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
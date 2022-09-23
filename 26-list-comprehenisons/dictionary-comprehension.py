import random

# Dictionary comprehension

# Generate random scores among students
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(0, 100) for student in students}
print(student_scores)

# Now, create a new dictionary of the students that scored above the pass
# threshold
passed_students = {
    student: score for (student, score) in student_scores.items() if score >= 70
}

print(passed_students)

# Interactive coding challege
# ------------------------------------
# You are going to use Dictionary Comprehension to create a dictionary called
# result that takes each word in the given sentence and calculates the number
# of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

letter_dict = {word.lower(): len(word) for word in sentence.split(" ")}
print(letter_dict)


# Interactive coding challege
# ------------------------------------
# You are going to use Dictionary Comprehension to create a dictionary called
# weather_f that takes each temperature in degrees Celsius and converts it into
# degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

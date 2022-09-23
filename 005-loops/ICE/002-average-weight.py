student_heights = [180, 124, 165, 173, 189, 169, 146]

count = 0
sum_heights = 0

for student_height in student_heights:
    sum_heights += student_height
    count += 1   

averageHeight =  sum_heights / count

print(f"The average height of the students is {round(averageHeight,0)}")

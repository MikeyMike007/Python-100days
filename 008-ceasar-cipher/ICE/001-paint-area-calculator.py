import math

def paint_calc(width, height, cover):
    print(math.ceil(width * height / cover))



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# Day 3 - 30 Days of Python Challenge
# STEPS 8 - 11

# slope calculations for line y = 2x - 2
# (0, -2) and (1, 0)
y1, y2 = -2, 0
x1, x2 = 0, 1
slope1 = (y2 - y1) / (x2 - x1)
print('The slope of the line is: ', slope1)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
print('The slope of the line is: ', slope2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('The distance between the two points is: ', distance)

print('(slope of line 1) > (slope of line 2) is: ', slope1 > slope2)

x3 = 0
y3 = x3**2 + 6*x3 + 9
print('The value of y when x is 0 is: ', y3)

x4 = 2
y4 = x4**2 + 6*x4 + 9
print('The value of y when x is 2 is: ', y4)
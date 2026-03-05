# Day 3 - 30 Days of Python Challenge

# TASKS 1 - 7
age = 26
height = 1.75
complex = 1 + 2j

# triangle calculations
print('Enter base: ')
base = float(input())
print('Enter height: ')
height = float(input())

area_of_triangle = 0.5 * base * height
print('The area of the triangle is: ', area_of_triangle)

print('Enter side a: ')
a = float(input())
print('Enter side b: ')
b = float(input())
print('Enter side c: ')
c = float(input())

perimeter_of_triangle = a + b + c
print('The perimeter of the triangle is: ', perimeter_of_triangle)

# rectangle calculations
print('Enter length: ')
length = float(input())
print('Enter width: ')
width = float(input())

area_of_rectangle = length * width
print('The area of the rectangle is: ', area_of_rectangle)  
circum_of_rectangle = 2 * (length + width)
print('The circumference of the rectangle is: ', circum_of_rectangle)

# circle calculations
print('Enter radius: ')
radius = float(input())
area_of_circle = 3.14 * radius ** 2
print('The area of the circle is: ', area_of_circle)
circum_of_circle = 2 * 3.14 * radius
print('The circumference of the circle is: ', circum_of_circle)




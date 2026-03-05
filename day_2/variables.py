# Day 2 - 30 Days of Python Challenge

# LEVEL 1
first_name = 'Mahya'
last_name = 'Waddell'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'Austin'
age = 26
year = 2026
is_married = False
is_true, is_light_on = True, True

# LEVEL 2
print(type(first_name))
print(type(age))
print(type(is_married))

print('Length of first_name:', len(first_name))
print('Length of last_name:', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_two / num_one
modulus = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

r = 30
pi = 3.14
area_of_circle = pi * r ** 2
circum_of_circle = 2 * pi * r

print("Input radius: ")
r = float(input())
area_of_circle = pi * r ** 2
circum_of_circle = 2 * pi * r
print("Area of circle: ", area_of_circle)
print("Circumference of circle: ", circum_of_circle)

print('Enter your first name: ')
first_name = input()
print('Enter your last name: ')
last_name = input()
print('Enter your country: ')
country = input()
print('Enter your city: ')
city = input()
print('Enter your age: ')
age = int(input())

print(first_name, last_name, city, country, age)
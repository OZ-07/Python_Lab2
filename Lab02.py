# define variables; name, age, height,favorite color
# from math import pi
import math
from math import degrees

#1
name = "toshiro_ozawa"
print (name)

age = 20
print(age)

height = 5.6
print(height)
print((height*12)+6) # in inches
height_inches= (5*12)+6
favorite_color = "green"
print(favorite_color)

# print(f"hello: {name} my is {favorite color}!")
print(f"hello:my name is {name} and my {favorite_color} is my favorite_color!")
if (name, age, height):
    print(f"you have {name}, {age}, {height}")
# print format specifiers within a multi-line string
#ex print(f"""
#       name: {name}
#       age: {age}
#       """)
print(f"""
name: {name}
age: {age}
""")
# extra space added when additional space added to the front
# create new variable, calculate area of circle with radius 5
# store result in variable circle_area
#print value only up to one decimal place
radius = 5
circle_area= math.pi*radius**2
print(circle_area)
print(round(circle_area,1))

#2

# make the square root of age
m= math.sqrt(age)
print(m)
print(f'square_root_height_is',round(m,3))
# use sin and cos on height
print(f'sine of height is, {math.sin(height):.5f}')
print(f'cos of height is, {math.cos(height):.5f}')

#3

#sum of age and 5
print(f'age+5= {age+5}')
#difference of height and 4
print(f'height-4{height-4}')
# product of age and height
print(f'age+height= {age+height}')
# the quotient of height and 2
print(f'height divide by 2 = {height/2}')
# the remainder of age divided by 3
print(f'remainder of age divided by 3= {age/3}')
# age raised to the power of two
print(f'age raised to the power of two= {age**2}')

#4

#temperature conversion
# farenheit to celcius
#def of yes_no (message):
 #   (yes_no = input(f"{message}(Y|N)").strip().upper())
  #  return yes_no != 'Y'
try:
    f =int(input(f"enter the temperature in farenheit").strip() )
    celsius= (f-32)*5/9
except ValueError as ve:
    print(ve)
print(f'{f} degrees in farenheit,as degrees {celsius} in celsius ')
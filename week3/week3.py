# # 1
# width = float(input("Enter the width of the rectangle: "))
# height = float(input("Enter the height of the rectangle: "))
# area = width * height
# print(f"The area of the rectangle with width {width} and height {height} is {area}.")
#
#
#
# # 2
# miles = float(input("Enter the number of miles driven: "))
# gallons = float(input("Enter the number of gallons used: "))
# mpg = miles / gallons if gallons != 0 else 0
# print(f"Your car's fuel efficiency is {mpg:.2f} MPG.")
#
#
#
#
# # 3
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5 / 9
# print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
#
#
#
#
# # 4
# start_day = int(input("Enter the starting day of the vacation (0-6, where 0=Sunday): "))
# vacation_length = int(input("Enter the length of the vacation in days: "))
# end_day = (start_day + vacation_length) % 7
# print(f"Your vacation will end on day number: {end_day}")
#
#
#
#
# # 5
# import math
#
# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle with radius {radius} is {circumference:.2f}.")
#
#
#
#
#
# # 6
# birth_year = int(input("Enter your birth year: "))
# current_year = 2024
# age = current_year - birth_year
# print(f"You are {age} years old (based on the year {current_year}).")
#
#
#
#
# # 7
# import turtle
#
# screen = turtle.Screen()
# screen.title("Draw a Square")
#
# pen = turtle.Turtle()
# pen.speed(2)
#
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)
#
# screen.mainloop()
#
#
#
#
#

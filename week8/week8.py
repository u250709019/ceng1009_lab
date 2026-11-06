# def g(x):
#     if x < 60:
#         return "F"
#     elif x < 70:
#         return "D"
#     elif x < 80:
#         return "C"
#     elif x < 90:
#         return "B"
#     else:
#         return ("A")
#
# input = int(input(("Enter grade: ")))
# print("your grade", g(input))






# def color(x):
#     if x >= 200:
#         return "red"
#     elif x >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# import turtle
#
# def bar(t, height, gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write(" " + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(color(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def chart(data):
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars
#     top = max_height + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         bar(t, height, gap)
#
#     wn.exitonclick()
#
#
# data = [15,100,250,180,40]
# chart(data)






# def color(x):
#     if x >= 200:
#         return "red"
#     elif x >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# import turtle
#
# def bar(t, height, gap):
#
#     if(height >= 0):
#         labely = height + gap
#     else:
#         labely = gap
#
#     t.penup()
#     t.left(90)
#     t.forward(labely)
#     t.write(" " + str(height))
#     t.backward(labely)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(color(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def chart(data):
#     max_height = max(data)
#     if min(data) < 0:
#         min_height = min(data)
#     else:
#         min_height = 0
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars
#     top = max_height + 4 * border
#     wn.setworldcoordinates(-border, -border + min_height, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         bar(t, height, gap)
#
#     wn.exitonclick()
#
# data = [-120,122,200,50,-40]
#
# chart(data)





#
#
# import math
#
# def findHypot(a,b):
#     hypot = (a**2 + b**2)**0.5
#     return hypot
#
# def calcwithmath(a,b):
#     hypot =math.hypot(a,b)
#     return hypot
#
# print(findHypot(3,4))
# print(calcwithmath(3,4))





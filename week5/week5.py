# import random
#
# for s in range(10):
#     print(random.randint(1,10))


# import random
#
# for s in range(10):
#     print(random.randint(25,35))

# import math as m
#
# a = int(input("giv us the first length: "))
# b = int(input("giv us the second length: "))
#
# def hh(x,y):
#     x = m.hypot(x,y)
#     return x
#
# print(hh(a,b))


# import math as m
#
# x = int(input("Enter the r of the circle: "))
#
# def a(s):
#     d = m.pi*s**2
#     return d
# h = a(x)
# print(f"result is {h}")


#
# import turtle as t
#
# def s():
#     for g in range(5):
#         t.forward(100)
#         t.right(144)
#
# s()
# t.done()



# import turtle as l
#
# def draw(l,g):
#     for i in range(4):
#         l.forward(g)
#         l.left(90)
#
# draw(l,100)
# l.done()


import turtle

def draw(l,g):
    for i in range(4):
        l.forward(g)
        l.left(90)
l = turtle.Turtle()

l.bgcolor("green")
l.color("blue")

for i in range(20,120,20):
    draw(l,i)
    l.penup()
    l.forward(12)
    l.left(90)
    l.forward(12)
    l.right(90)

    l.pendown()
    l.exitonclick()








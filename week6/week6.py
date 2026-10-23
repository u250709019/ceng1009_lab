import turtle as t


screen = t.Screen()
screen.bgcolor("green")

turtle = t.Turtle()


def draw(turtle,sides,size):
    angle = 360/sides
    turtle.pensize(3)
    for s in range(sides):
        turtle.forward(size)
        turtle.left(angle)

    screen.exitonclick()


def sup(turtle,angle):
    size = 5
    for h in range(100):
        turtle.forward(size)
        size +=2
        turtle.left(angle)


def sky(turtle, angle):
    angle = 144
    for s in range(5):
        turtle.forward(50)
        turtle.right(angle)


def drawSprite(someturtle , legs ,length):
    angle= 360/legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.back(length)
        someturtle.left(angle)


# turtle.pencolor("blue")
# draw(turtle,8,50)


# turtle.penup()
# turtle.goto(-150,0)
# turtle.pendown()
#
# sup(turtle,90)



# turtle.pensize(2)
# turtle.pencolor("blue")
# turtle.penup()
# turtle.goto(-150,0)
# turtle.pendown()
#
# sup(turtle,91)



# for s in range(5):
#     sky(turtle,144)
#     turtle.penup()
#     turtle.forward(150)
#     turtle.pendown()
#     turtle.right(144)



# drawSprite(turtle,15 ,120)






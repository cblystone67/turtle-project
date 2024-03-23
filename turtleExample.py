import turtle


wn = turtle.Screen()
wn.bgcolor("lightgrey")
wn.title("Chris Blystone")


def draw_arc(turtle, size, curves, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    for points in range(curves):
        turtle.forward(size/curves*points)
        turtle.right(90/curves * points)


def draw_shape(turtle, size, curves, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    for points in range(curves):
        turtle.backward(size/curves * 20)
        turtle.left(20/curves * points)


def create_turtle(turtle, paint, w):
    turtle.shape("turtle")
    turtle.color(paint)
    turtle.speed(15)
    turtle.width(w)


def draw_swivel():
    i = 0
    colorlist = ["violet", "blue", "indigo",
                 "yellow", "black", "white", "green", "purple"]
    for c in colorlist:
        colorlist[i] = turtle.Turtle()
        create_turtle(colorlist[i], c, 18)
        draw_shape(colorlist[i], 20, 8, (-315 + 10 * i), 260)
        i += 1


def draw_rainbow():
    i = 0
    colorlist = ["red", "orange", "yellow",
                 "green", "blue", "indigo", "violet"]
    for c in colorlist:
        colorlist[i] = turtle.Turtle()
        create_turtle(colorlist[i], c, 25)
        draw_arc(colorlist[i], 275, 10, (-200 + 10 * i), -100)
        i += 1


draw_rainbow()
draw_swivel()

turtle.done()

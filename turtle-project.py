# from turtle import *
import turtle
skk = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("white")
skk.color("blue")
skk.shape("turtle")
skk.turtlesize(2, 2, 2)
wn.title("turtle")
# turtle position


def leftTopCorner():
    postion(-340, 325)  # top left hand corner.


def rightTopCorner():
    postion(295, 325)  # top right hand corner


def bottomRightCorner():
    postion(295, -275)  # bottom right hand corner


def bottomLeftCorner():
    postion(-340, -275)  # bottom left hand corner.


def postion(x, y):
    skk.penup()
    skk.goto(x, y)
    skk.pendown()

# star


def star(length):
    skk.right(75)
    skk.forward(length)
    for i in range(4):
        skk.right(144)
        skk.forward(length)

# rectangle


def rectangle(length):
    for i in range(4):
        skk.forward(length)
        skk.right(90)


star(100)
rightTopCorner()
star(50)


turtle.done()

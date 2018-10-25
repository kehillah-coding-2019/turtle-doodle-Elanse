import turtle

import math

bg = turtle.Screen()
cross = turtle.Turtle()
cross2 = turtle.Turtle()

diagonal = turtle.Turtle()
diagonal1 = turtle.Turtle()
diagonal2 = turtle.Turtle()
diagonal3 = turtle.Turtle()

line = turtle.Turtle()
line1 = turtle.Turtle()
line2 = turtle.Turtle()
line3 = turtle.Turtle()

height = 400
aspectRatio = 2/1 #sets the flag to a 2:1 ratio
length = aspectRatio * height


bg.setup(length, height) #sets flag dimensions in a 2:1 aspectRatio
bg.bgcolor("midnightblue")


def drawLine(myTurtle, color, size, x, y, length, angle):
    """
    Make a function to draw the lines on the Union Jack.
    """
    myTurtle.speed(0)
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.pencolor(color)
    myTurtle.pensize(size)
    myTurtle.begin_fill()
    myTurtle.right(angle)
    myTurtle.forward(length)
    myTurtle.end_fill()
    myTurtle.ht()

drawLine(cross, "white", height/5, -400, 200, 900, 26.7) # first white cross
drawLine(cross2, "white", height/5, 400, 200, 900, 153.3) # second white cross
drawLine(diagonal, "red", height/15, -413.3, 200, 425, 26.7) # top left
drawLine(diagonal1, "red", height/15, 386.7, 200, 425, 153.3) # top right
drawLine(diagonal2, "red", height/15, -386.7, -200, 425, -26.7) # bottom left
drawLine(diagonal3, "red", height/15, 413.3, -200, 425, -153.3) # bottom right
drawLine(line, "white", height/3, 0, 200, 400, 90) # white vertical line
drawLine(line1, "white", height/3, -400, 0, 800, 0) # white horizontal line
drawLine(line2, "red", height/5, 0, 200, 400, 90) # red vertical line
drawLine(line3, "red", height/5, -400, 0, 800, 0) # red horizontal line

input()

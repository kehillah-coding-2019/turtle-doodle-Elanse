import turtle

import math

bg = turtle.Screen()
cross = turtle.Turtle()
cross2 = turtle.Turtle()

diagonal = turtle.Turtle()
diagonal1 = turtle.Turtle()
diagonal2 = turtle.Turtle()
diagonal3 = turtle.Turtle()

height = 400
aspectRatio = 2/1 #sets the flag to a 2:1 ratio
length = aspectRatio * height


bg.setup(length, height) #sets flag dimensions in a 2:1 aspectRatio
bg.bgcolor("midnightblue")


"""
Make a function to draw the diagonal lines on the Union Jack with four parameters:
myTurtle, location on x axis, location on y axis, and angle of the line
"""

def diagonalLine(myTurtle, color, size, x, y, length, angle):
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

diagonalLine(cross, "white", height/5, -400, 200, 900, 26.7) # first white cross
diagonalLine(cross2, "white", height/5, 400, 200, 900, 153.3) # second white cross
diagonalLine(diagonal, "red", height/15, -413.3, 200, 425, 26.7) # top left
diagonalLine(diagonal1, "red", height/15, 386.7, 200, 425, 153.3) # top right
diagonalLine(diagonal2, "red", height/15, -386.7, -200, 425, -26.7) # bottom left
diagonalLine(diagonal3, "red", height/15, 413.3, -200, 425, -153.3)




input()

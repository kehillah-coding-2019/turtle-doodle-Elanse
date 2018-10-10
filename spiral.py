import turtle
from itertools import cycle

t = turtle.Turtle()
t.speed(0)

COLOR_CHOICES = ["red", "orange", "yellow", "green", "blue", "purple"]

colors = cycle(COLOR_CHOICES)

def drawSpiral(myTurtle, x, y):
    for i in range(0, 500, 5):
        myTurtle.penup()
        myTurtle.setpos(x, y)
        myTurtle.color(next(colors))
        myTurtle.pendown()
        myTurtle.circle(i)
        myTurtle.left(10)

drawSpiral(t, 0, 0)

input()

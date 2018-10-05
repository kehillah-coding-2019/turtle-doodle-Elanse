import turtle

bg = turtle.Screen()
cross = turtle.Turtle()

height = 400
aspectRatio = 2/1 #sets the flag to a 2:1 ratio
length = aspectRatio * height

bg.setup(length, height) #sets flag dimensions in a 2:1 aspectRatio
bg.bgcolor("midnightblue")


"""
Make a function to draw the diagonal lines on the Union Jack.
"""

def diagonalLine(myTurtle, x, y, angle):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.pencolor("white")
    myTurtle.pensize(height/5)
    myTurtle.begin_fill()
    myTurtle.right(angle)
    myTurtle.forward(900)
    myTurtle.end_fill()
    myTurtle.ht()

diagonalLine(cross, -400, 200, 26.7)

input()

import turtle

bg = turtle.Screen()
cross = turtle.Turtle()

bg.screensize(1080, 540, "midnightblue") #sets flag background

"""
Make a function to draw the diagonal lines on the Union Jack
"""

def crossingLines(myTurtle):
    myTurtle.penup()
    myTurtle.goto(-540, 270)
    myTurtle.pendown()

    myTurtle.pencolor("white")
    myTurtle.pensize(108)
    myTurtle.begin_fill()
    myTurtle.right(45)
    myTurtle.forward(1207.5)
    myTurtle.end_fill()

input()

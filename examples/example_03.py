"""
turtle doodle by aemerritt
"""

import turtle
myTurtle = turtle.Turtle()
myOtherTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.hideturtle()
myOtherTurtle.hideturtle()
myOtherTurtle.speed(0)

#I created two turtles, hid them, and boosted their speeds

colors = [
(1.00, 0.00, 0.00), (1.00, 0.50, 0.00), (1.00, 1.00, 0.00), (0.00, 1.00, 0.00), (0.00, 0.00, 1.00), (0.95, 0.00, 1.00)
]

#This creates a color index for my turtles to draw from later

def drawCircle(myTurtle, sideLength):
	myTurtle.circle(sideLength)

#I defined a function that will allow my turtle to quickly make a circle

def drawSpiral(myTurtle):
	for sideLength in range (1,301):
		index = int(sideLength)
		color = colors[index%6]
		myTurtle.color(color)
		drawCircle(myTurtle, sideLength)
		myTurtle.right(45)

#A lot is happening here. This function incorporates the previous circle function.
#It also taps into the color index.  It makes it so that each time it rotates, it draws a new circle and changes colors.

def drawNestedSquare(myOtherTurtle):
	for sideLength2 in range(630, 407, -10):
		pos = myOtherTurtle.position()
		myOtherTurtle.up()
		myOtherTurtle.goto(pos[0]+5,pos[1]-5)
		myOtherTurtle.down()
		for i in range(4):
			myOtherTurtle.forward(sideLength2)
			myOtherTurtle.right(90)

#This function has a nested loop in it.  It draws a series of concentric squares.
#After each square, it picks up the turtle, moves it to a new spot, and draws a new one.
#The range makes it so that it starts in the very corner and ends at the tip of the flower.

drawSpiral(myTurtle)
myOtherTurtle.up()
myOtherTurtle.goto(-319,319)
myOtherTurtle.down()
drawNestedSquare(myOtherTurtle)
input()

#This calls the functions into action. It draws the circle spiral first.
#Then, it picks up the second turtle, moves it to the corner, and begins drawing the squares.
#That concludes the drawing.

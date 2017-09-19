"""
turtle doodle by jnozik
"""

import turtle

# Draw the star.

def commuStar(turtle,angle,sideLength,sides,bg):

	# Change these to change the background color of the drawing and the color of the star.
	backgroundColor = "red"
	turtleColor = "yellow"



	bg.bgcolor(backgroundColor)

	x = sideLength * -.5 # Centers the star on the horizontal plane.

	turtle.up()
	turtle.goto(x,-x) # Move the turtle to coordinates defined as half the sidelength.
	turtle.down()

	turtle.color(turtleColor)

	turtle.begin_fill()
	for star in range(sides): # Number of sides.
		turtle.forward(sideLength) # Length of sides.
		turtle.right(angle) # Turn angle to make the star (144 along with 5 sides will produce a five-pointed star).
	turtle.end_fill()

# Define the turtles trotsky and lenin and call the function commuStar.
trotsky = turtle.Turtle()
lenin = turtle.Screen()
commuStar(trotsky,144,440,5,lenin)

def manyShapes(turtle,shapeLength,numRepeat): # Takes a turtle object, length of the sides of the squares, and how many to make.
	# Change the starting point of the pattern.
	xinit = -200
	yinit = -200

	turtleSpeed = 0 # Change the speed of the turtle drawing the pattern.

	a = 0
	b = 5 # Change this to increase or decrease the amount by which the shape side length changes.
	forward = 3 # Change this to increase or decrease the distance between each shape.
	firstSquare = "yellow" # Change the color of the first square in the pattern.
	secondSquare = "#C7C728" # Change the color of the second square in the pattern.

	turtle.speed(turtleSpeed)
	z = 360/numRepeat # Adjusts the left angle movement based on the number of squares so that it always completes a circle.
	# Moves the turtle to its starting position.
	turtle.up()
	turtle.goto(xinit,yinit)
	turtle.down()

	for shapes in range(numRepeat): # Draw the shapes.
		for indivShape in range(4):
			turtle.forward(shapeLength+a)
			turtle.right(90)
		# Changes every other square to be a slightly darker shade of yellow.
		if shapes % 2 == 0:
			turtle.color(secondSquare)
		else:
			turtle.color(firstSquare)
		a = a + b # Changes the sidelength of the shape for the next iteration.
		turtle.forward(forward)
		turtle.left(z)

	# Moves the turtle to the spot opposite of its original location to mirror the pattern.
	turtle.up()
	turtle.goto((xinit * -1),(yinit * -1))
	turtle.down()

	# This loop is identical to the one directly before, except it turns to the right instead of the left.
	for moreShapes in range(numRepeat):
		for indivShapes in range(4):
			turtle.forward(shapeLength+a)
			turtle.left(90)
		if moreShapes % 2 == 0:
			turtle.color(secondSquare)
		else:
			turtle.color(firstSquare)
		a = a + b
		turtle.forward(forward)
		turtle.right(z)

manyShapes(trotsky,20,100)
turtle.exitonclick()

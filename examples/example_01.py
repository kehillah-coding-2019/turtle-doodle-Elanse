import turtle


twisty = turtle.Turtle()
twisty.speed(0)
twisty.color('purple')


for n in range(9):
    twisty.forward(60)
    twisty.right(170)
    twisty.forward(75)
    twisty.right(30)
twisty.hideturtle()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="example_0.eps")

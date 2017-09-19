import turtle


rainbow = turtle.Turtle()
rainbow.speed(0)
rainbow.color('purple')


for n in range(30):

    #generate three numbers between zero and one
    r = n/30
    g = (30-n)/30
    b = (30-n)/30
    
    print(r, g, b) #check output in terminal
    rainbow.color(r, g, b) #set color of turtle to r,g,b triplet
    rainbow.forward(60)
    rainbow.right(175)
    rainbow.forward(75)
    rainbow.right(36)
rainbow.hideturtle()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="example_02.eps")
input()

# Elan's Turtle Doodle 
This folder contains two doodles. One of the doodles draws the Union Jack, the official flag United Kingdom, when run. The other draws a spiral of circles that cycles through the colors of the rainbow. 
### Union Jack
![image](https://user-images.githubusercontent.com/33039002/46832900-1eaade80-cd5c-11e8-8d51-ee5f93328d0d.png)
### Spiral
![image](https://user-images.githubusercontent.com/33039002/46832296-83653980-cd5a-11e8-9338-df25350e85c6.png)
## How to Run
To run, use the python interpreter with doodle.py (draws the Union Jack) or spiral.py (draws a spiral). Your terminal window should look like this:
```
$python3 doodle.py
```
OR
```
$python3 spiral.py
```
## Highlighted Code
### doodle.py
This code creates all the lines on the Union Jack.
```python
def drawLine(myTurtle, color, size, x, y, length, angle):
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
```
### spiral.py
The cycle mod lets in cycle through the colors of the rainbow easily.
```python
import cycle
COLOR_CHOICES = ["red", "orange", "yellow", "green", "blue", "purple"] # colors used in the spiral
colors = cycle(COLOR_CHOICES) # cycles through the colors 
```

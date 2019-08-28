# example of creating and using functions in python
import turtle

my_turtle = turtle.Turtle()

def createSquare():
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)

createSquare()
my_turtle.left(100)
createSquare()

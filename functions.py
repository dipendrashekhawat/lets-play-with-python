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

# function call
createSquare()


# function with parameters

def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

square(200, 90)

# calling function in a Loop

for i in range(4):
    square(50, 90)


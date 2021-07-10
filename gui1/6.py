import turtle

wn=turtle.Screen()
pen = turtle.Turtle()
sides=6
length=70

angle=360//sides
for i in range (sides):
    pen.forward(length)
    pen.right(angle)
turtle.done()


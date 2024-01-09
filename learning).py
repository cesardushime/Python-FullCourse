import turtle

animation = turtle.Turtle()
animation.speed(0)
animation.getscreen().bgcolor("black")
animation.color("aqua")
animation.hideturtle()
for i in range(160):
    animation.circle(i)
    #animation.backward(6)  # Use right() function to rotate the turtle
    #animation.forward(3)
    #animation.right(6)
    animation.right(6)

turtle.done()

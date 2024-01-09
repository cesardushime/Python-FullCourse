import turtle

# Create a turtle screen and turtle object
screen = turtle.Screen()
building = turtle.Turtle()
building.speed(0)

# Function to draw a rectangle
def draw_rectangle(turtle, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a staircase
def draw_stairs(turtle, x, y, stairs, width, height, color):
    for _ in range(stairs):
        draw_rectangle(turtle, width, height, color)
        turtle.penup()
        turtle.goto(x, y)
        x += width
        y += height
        turtle.pendown()

# Function to draw a car
def draw_car(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(turtle, 70, 20, "blue")
    turtle.penup()
    turtle.goto(x + 10, y + 20)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(10)
    turtle.penup()
    turtle.goto(x + 50, y + 20)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(10)

# Draw the building (two floors)
building.penup()
building.goto(-100, -100)
building.pendown()
draw_rectangle(building, 200, 150, "gray")

building.penup()
building.goto(-80, -100)
building.pendown()
draw_rectangle(building, 40, 100, "lightblue")

building.penup()
building.goto(40, -100)
building.pendown()
draw_rectangle(building, 40, 100, "lightblue")

building.penup()
building.goto(-60, -100)
building.pendown()
draw_rectangle(building, 20, 50, "gray")

building.penup()
building.goto(-20, -100)
building.pendown()
draw_rectangle(building, 20, 50, "gray")

building.penup()
building.goto(20, -100)
building.pendown()
draw_rectangle(building, 20, 50, "gray")

# Draw stairs
building.penup()
building.goto(-120, -100)
building.pendown()
draw_stairs(building, -120, -100, 3, 40, 50, "lightblue")

# Draw the front yard
building.penup()
building.goto(-150, -100)
building.pendown()
draw_rectangle(building, 50, 50, "green")

building.penup()
building.goto(100, -100)
building.pendown()
draw_rectangle(building, 50, 50, "green")

# Draw pathway to parking
building.penup()
building.goto(-200, -150)
building.pendown()
draw_rectangle(building, 50, 200, "black")

building.penup()
building.goto(150, -150)
building.pendown()
draw_rectangle(building, 50, 200, "black")

# Draw cars parked in front of the building
draw_car(building, -140, -110)
draw_car(building, -90, -110)
draw_car(building, -40, -110)

building.hideturtle()
turtle.done()

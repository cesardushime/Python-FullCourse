import turtle as trtl
import random as rand

# -----setup-----
# Your setup code...

# Your draw_apple function...

# Rest of your functions...

# Function to update score...

# Your alphabet list...

# Create turtles and set up apples and their corresponding letters
apple_image = "apple.gif"
wn = trtl.Screen()
wn.setup(width=.35, height=.4)
wn.bgpic("background.gif")
wn.addshape(apple_image)

apples = {}
letters = {}

def create_apple(x, y):
    new_apple = trtl.Turtle()
    new_apple.penup()
    new_apple.goto(x, y)
    apples[new_apple] = ' '
    letters[new_apple] = trtl.Turtle(visible=False)
    letters[new_apple].penup()
    letters[new_apple].goto(x, y - 20)
    return new_apple

# Create apples and their corresponding letters
positions = [-150, -80, -10, 60, 130]
for i in range(5):
    apple = create_apple(positions[i], 0)
    x = rand.choice(alphabet)
    apples[apple] = x
    letters[apple].write(x, font=("Arial", 20, "bold"))

# Function to drop the apple and handle user input
def fall(active_apple):
    def fall_wrapper():
        nonlocal active_apple
        letter = apples[active_apple]
        letters[active_apple].clear()

        while active_apple.ycor() >= -150:
            active_apple.sety(active_apple.ycor() - 1)
            if active_apple.ycor() <= -150:
                x = rand.choice(alphabet)
                apples[active_apple] = x
                letters[active_apple].write(x, font=("Arial", 20, "bold"))
                wn.onkeypress(None, x)
                wn.onkeypress(fall(active_apple), x)
                break

        draw_apple(active_apple)

    return fall_wrapper

# Update all onkeypress events for each apple
for apple in apples:
    x = apples[apple]
    wn.onkeypress(fall(apple), x)

# Rest of your code...

# Function to display instructions...

# Keyboard binding for quitting the game...

wn.listen()
wn.mainloop()

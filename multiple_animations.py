from tkinter import *
from Ball import *
import pygame
import threading
import time
def play_music():
    pygame.init()
    pygame.mixer.music.load('music_background.mp3')
    pygame.mixer.music.play()

def animate_balls():
    window = Tk()
    window.title("multiple animations")
    WIDTH = 500
    HEIGHT = 500

    canvas = Canvas(window, width=WIDTH, height=HEIGHT)
    canvas.pack()

    volley_ball = Ball(canvas, 0, 0, 100, 10, 5, "cyan")
    tennis_ball = Ball(canvas, 0, 0, 50, 4, 7, "yellow")
    basket_ball = Ball(canvas, 0, 0, 105, 8, 7, "orange")
    hand_ball = Ball(canvas, 0, 0, 90, 5, 4, "black")
    foot_ball = Ball(canvas, 0, 0, 95, 3, 9, "pink")
    base_ball = Ball(canvas, 0, 0, 70, 5, 4, "darkgrey")

    while True:
        volley_ball.move()
        tennis_ball.move()
        basket_ball.move()
        hand_ball.move()
        foot_ball.move()
        base_ball.move()
        window.update()
        time.sleep(0.01)

    window.mainloop()

# Create and start threads for music and animation
music_thread = threading.Thread(target=play_music)
music_thread.start()

animation_thread = threading.Thread(target=animate_balls)
animation_thread.start()

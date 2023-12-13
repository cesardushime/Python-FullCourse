from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, x, y, diameter, dx, dy, color, letter):
        self.canvas = canvas
        self.letter = letter
        self.text_id = canvas.create_text(x, y, text=letter, font=("Arial", 12))
        self.id = canvas.create_oval(x, y, x + diameter, y + diameter, fill=color)
        self.dx = dx
        self.dy = dy

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        self.canvas.move(self.text_id, self.dx, self.dy)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= 800:  # Check if ball hits left or right edge
            self.dx = -self.dx
        if pos[1] <= 0 or pos[3] >= 600:  # Check if ball hits top or bottom edge
            self.dy = -self.dy


class BallGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Type the Ball's Letter")
        self.WIDTH = 800
        self.HEIGHT = 600
        self.canvas = Canvas(self.master, width=self.WIDTH, height=self.HEIGHT, bg="#f0f0f0")
        self.canvas.pack()
        self.balls = []
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.create_balls()
        self.master.bind("<Key>", self.check_input)
        self.score = 0
        self.score_label = Label(self.master, text="Score: 0", font=("Arial", 12))
        self.score_label.pack()
        self.start_time = time.time()

    def create_balls(self):
        for _ in range(20):
            x = random.randint(50, self.WIDTH - 50)
            y = random.randint(50, self.HEIGHT - 50)
            diameter = random.randint(60, 120)
            dx = random.choice([-5, -4, -3, 3, 4, 5]) * 10
            dy = random.choice([-5, -4, -3, 3, 4, 5]) * 10
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            letter = random.choice(self.letters)
            ball = Ball(self.canvas, x, y, diameter, dx, dy, color, letter)
            self.balls.append(ball)

    def check_input(self, event):
        user_text = event.char.upper()
        for ball in self.balls:
            if user_text == ball.letter:
                self.canvas.delete(ball.id)
                self.canvas.delete(ball.text_id)
                self.balls.remove(ball)
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                break

        if not self.balls:
            self.end_time = time.time()
            duration = self.end_time - self.start_time
            self.show_results(duration)

    def show_results(self, duration):
        result_window = Toplevel(self.master)
        result_window.title("Game Over")

        score_label = Label(result_window, text=f"Final Score: {self.score}", font=("Arial", 12))
        score_label.pack()

        duration_label = Label(result_window, text=f"Time Spent: {duration:.2f} seconds", font=("Arial", 12))
        duration_label.pack()

        play_again_button = Button(result_window, text="Play Again", command=self.reset_game)
        play_again_button.pack()

        quit_button = Button(result_window, text="Quit", command=self.master.quit)
        quit_button.pack()

    def reset_game(self):
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.start_time = time.time()
        self.create_balls()


def main():
    root = Tk()
    game = BallGame(root)

    while True:
        for ball in game.balls:
            ball.move()
            root.update()
            root.after(30)


if __name__ == "__main__":
    main()

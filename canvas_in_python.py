from tkinter import *

window = Tk()
canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0,0,500,500, fill="blue")
# canvas.create_line(0,500,500,0, fill="red")
canvas.create_rectangle(50, 50, 250, 250, fill="purple", outline="black")
canvas.create_arc(50, 50, 250, 250, fill="yellow")
canvas.pack()

window.mainloop()

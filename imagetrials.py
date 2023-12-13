from tkinter import *
from PIL import Image, ImageTk

# Convert the JPEG image to a PNG format
img = Image.open('car.jpeg')
img.save('car.png')

# Use the converted image in your Tkinter code
window = Tk()
image = ImageTk.PhotoImage(file='car.png')
label = Label(window, image=image)
label.pack()

window.mainloop()

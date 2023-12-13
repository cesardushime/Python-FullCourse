from tkinter import *
from tkinter import *
from PIL import Image, ImageTk
import time

# Convert the JPEG image to a PNG format
img = Image.open('ufo.png')
img = img.resize((100,100))
img.save('ufo.png')
imagespace = Image.open('space_image.jpeg')
imagespace = imagespace.resize((500,500))
imagespace.save('space_image.png')

# creating a constant, and it should all be in uppercase
WIDTH = 500
HEIGHT = 500
xVELOCITY = 10
yVELOCITY = 5

window = Tk()
window.title("Animations")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='space_image.png', height=500,width=500)
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:  # it will continue until we close up our program
    coordinates = canvas.coords(my_image)
    print(coordinates)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVELOCITY = -xVELOCITY
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVELOCITY = -yVELOCITY

    canvas.move(my_image, xVELOCITY, yVELOCITY)

    window.update()
    time.sleep(0.01)

window.mainloop()

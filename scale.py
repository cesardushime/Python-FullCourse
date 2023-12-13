from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+" degrees C")

window = Tk()

scale = Scale(window,
              from_=100, to=0,
              length=400,
              orient=VERTICAL,
              font=('Consolas',16),
              tickinterval=10,
              troughcolor='cyan',
              fg='pink',
              bg='black')
button = Button(window, text="submit",
                command=submit)

scale.pack()
button.pack(side=RIGHT)


window.mainloop()
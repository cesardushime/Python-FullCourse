from tkinter import *

window = Tk()
window.geometry("420x420")
window.config(background="purple")
window.title("Cr GUI")

label = Label(window,
              text="Hello Buddies",
              font=('Arial',40,'bold'),
              fg='cyan',
              bg='black',
              padx=20,
              pady=20,
            )
label.place(x=0,y=0)
label.pack()

window.mainloop()


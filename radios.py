from tkinter import *

food = ["pizza","hamburger","hotdog"]

window = Tk()
x = IntVar()

for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index],
                            variable=x,
                            value=index,
                            padx=25,
                            pady=5,
                            font=("Arial",30))
    radiobutton.pack(anchor=W)


window.mainloop()
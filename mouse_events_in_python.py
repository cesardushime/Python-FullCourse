from tkinter import *

def doSomething(event):
    print("You did a thing!")
window = Tk()
#window.bind("<Button-1>",doSomething)  Left click
#window.bind("<Button-2>",doSomething)  #sroll wheel of the mouse
#window.bind("<Button-3>",doSomething) #Right click

#window.bind("<ButtonRelease>",doSomething)
#window.bind("<Enter>",doSomething) #entering the window
window.bind("<Leave>",doSomething) #leaving the window
window.bind("<Motion>",doSomething)


window.mainloop()
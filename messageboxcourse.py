from tkinter import *
from tkinter import messagebox
def click():
    pass
window = Tk()

#messagebox.showinfo(title='This is an info message')
if messagebox.askyesno(title='yes/no',message="Do you like cakes? "):
    print("I like cakes too!")
else:
    print("Why don't you like cakes? ")

button = Button(window,command=click,text="click me")
button.pack()
window.mainloop()
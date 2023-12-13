from tkinter import *

def submit():
    print("You have submitted successfully!")
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)
window = Tk()

entry = Entry(window,
              font=("Arial",40),
              fg="green",
              bg="cyan",
              show="*")
entry.pack(side=LEFT)
submit_button = Button(window,
                text="Submit",
                command=submit,
                font=("italic"),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                )
delete_button = Button(window,
                       text="delete",
                       command=delete)

backspace_button = Button(window,
                          text="backspace",
                          command=backspace)
backspace_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
submit_button.pack(side=RIGHT)
window.mainloop()
from tkinter import *

def display():

    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree")
window = Tk()

#python_photo = PhotoImage(file='python_photo.jpeg')

x = IntVar()

check_button = Checkbutton(window,
                           text="I agree to do something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial",20),
                           fg="cyan",
                           bg="black",
                           activeforeground="cyan",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           #image=python_photo,
                           #compound="top"
                           )
check_button.pack()
window.mainloop()
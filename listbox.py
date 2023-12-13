def submit():
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE
                  )

listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(2,"garlic bread")
listbox.insert(2,"soup")
listbox.insert(2,"salad")

entrybox=Entry(window)
entrybox.pack()
submit_button = Button(window, text="Submit",
                       command=submit)
add_button = Button(window, text="Add",
                       command=add)
delete_button = Button(window, text="Delete",
                       command=delete)
add_button.pack()
delete_button.pack()
submit_button.pack()

window.mainloop()
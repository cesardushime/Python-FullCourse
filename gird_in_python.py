from tkinter import *

window = Tk()
firstnameLabel= Label(window,text="First name: ").grid(row=0,column=0)
firstnameEntry= Entry(window).grid(row=0,column=1)

lastNameLabel= Label(window,text="Last name: ").grid(row=1,column=0)
lastNmaeEntry= Entry(window).grid(row=1,column=1)

emailLabel= Label(window,text="Email: ").grid(row=2,column=0)
emailEntry= Entry(window).grid(row=2,column=1)

submitButton = Button(window,text="Submit").grid(row=3,column=0,columnspan=2)
window.mainloop()
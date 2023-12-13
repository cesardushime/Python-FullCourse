from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\user\\PycharmProjects\\pythonfullcourse",
                                    defaultextension='.txt',
                                    filetypes=[("Text file", ".txt"),
                                               ("HTML file", ".html"),
                                               ("All files", ".*")])
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(window,text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
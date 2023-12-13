from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cutFile():
    print("You cut some file")
def copyFile():
    print("You have copied the file")
def pasteFile():
    print("You have pasted the file")
def bluetoothShare():
    print("You are sharing by bluetooth")
def nearbyShare():
    print("You are sharing by nearby share")
def xenderShare():
    print("You are sharing with Xender")
window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="open", command=openFile)
fileMenu.add_command(label="save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="edit",menu=editMenu)
editMenu.add_command(label="cut", command=cutFile)
editMenu.add_command(label="copy", command=copyFile)
editMenu.add_command(label="paste", command=pasteFile)

shareMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="share",menu=shareMenu)
shareMenu.add_command(label="bluetooth", command=bluetoothShare)
shareMenu.add_command(label="nearby", command=nearbyShare)
shareMenu.add_command(label="Xender", command=xenderShare)
window.mainloop()
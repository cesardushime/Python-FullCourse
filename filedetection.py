import os
path = "C:\\Users\\user\\OneDrive\\Desktop"

if os.path.exists(path):
    print("That locatioin exists!")
    #if os.path.isfile(path):
        #print("That is a file")
    if os.path.isdir(path):
        print("It is a directory")
else:
    print("That location doesn't exist!")
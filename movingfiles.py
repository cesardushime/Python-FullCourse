import os
path = "C:\\Users\\user\\OneDrive\\Desktop"
source = "test.txt"
destination = "C:\\Users\\user\\OneDrive\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print('Source was moved')
except FileNotFoundError:
    print(source+ "was not found")

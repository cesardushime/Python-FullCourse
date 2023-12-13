try:
    text = "You don't ever have to give up!!!!!!!!!!!!!"

    with open('test.txt', 'r') as file:
         print(file.read())
    with open("test.txt", 'w') as file:
        file.write(text)
    #name = "Brotheraaaaa"
    #with open("test.txt", 'a') as file:
        #file.write(name)

except FileNotFoundError:
    print("File was not found:")
'''**kwargs pack all the arguments in a dictionary, and we follow the usual rules to access and iterate over elements in a dictionary using values and a for loop'''

def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(first="Bro", middle="Dude", last="Code")
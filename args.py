'''args is a parameter that is packs all the arguments in a tuple, and it requires a for loop to iterate over it'''
def add(*args):
    sum = 0
    for i in args:
        sum += i  
    return sum
print(add(1,2,3,50))
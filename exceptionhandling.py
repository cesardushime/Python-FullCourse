# expception are all the events detected during execution that interrupt the flow of a program. To handle this you inclose the dangerous codes in a try module

try:
    numerator = int(input("Enter a number to diviide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("Can't divide by zero. Idiot!!")
except ValueError as e:
    print(e)
    print("Put only numbers, please!")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)

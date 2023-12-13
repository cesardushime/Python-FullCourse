# higher order functions accept functions as arguments
# Return a function

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello!")
    print(text)

hello(loud)
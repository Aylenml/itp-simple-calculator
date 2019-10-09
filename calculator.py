def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def divide(x, y):
    if y != 0:
        return x/y
    else: 
        return "Invalid value for denominator, cant't divide by 0!"


def multiply(x, y):
    return x*y


def square(x):
    return x*x


def power(x, y):
    if y == 0:
        return  1
    else:
        return x*power(x,y-1)

def sqrt(x):
    pass
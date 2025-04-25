numbers = input("Please enter your equation: ")

def addition(vars):
    for i in vars:
        i += i
    print(i)

def subtraction(vars):
    for i in vars:
        i -= i
    print(i)

def multiplication(vars):
    for i in vars:
        i *= i
    print(i)

def division(vars):
    for i in vars:
        i /= i
    print(i)

if "+" in numbers:
    array = numbers.split("+")
    array = [float(i) for i in array]
    addition(array)
elif "-" in numbers:
    array = numbers.split("-")
    array = [float(i) for i in array]
    subtraction(array)
elif "*" in numbers:
    array = numbers.split("*")
    array = [float(i) for i in array]
    multiplication(array)
elif "/" in numbers:
    array = numbers.split("/")
    array = [float(i) for i in array]
    division(array)
else:
    print ("Symbols available: + - / *")
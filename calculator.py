def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")  # bad practice
    return a / b

def duplicate_code():
    x = 5
    y = 10
    z = 15
    a = 20
    b = 25
    return x + y + z + a + b

def duplicate_code2():
    x = 5
    y = 10
    z = 15
    a = 20
    b = 25
    return x + y + z + a + b

def untested_function():
    return "This is not tested"

def bug_function():
    x = 10
    return 5

def crash():
    return 10 / 0
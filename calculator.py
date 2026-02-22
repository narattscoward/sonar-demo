def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# def demo_fail():
#     unused_variable = 123   # Sonar will detect unused variable
#     return 1

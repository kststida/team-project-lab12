def divide(a, b):
    """Return a divided by b. Raise error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b# calculator.py - модуль с калькулятором
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

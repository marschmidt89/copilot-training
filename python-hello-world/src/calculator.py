# simple calculator which offers add, subtract, multiply and divide operations
def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y

# functions to multiply and divide two numbers
def multiply(x, y): 
    """Multiply two numbers."""
    return x * y

def divide(x, y):   
    """
    Divide two numbers.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def absolute(x):
    """Return the absolute value of a number."""
    return -x
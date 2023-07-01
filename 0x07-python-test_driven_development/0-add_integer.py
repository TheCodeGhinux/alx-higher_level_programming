#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers and returns the sum.
    
    Parameters:
    a (int or float): First integer or float.
    b (int or float): Second integer or float. Default value is 98.
    
    Returns:
    int: The addition of a and b.
    
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise TypeError if a or b is not an integer or float
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Return the sum of a and b
    return a + b

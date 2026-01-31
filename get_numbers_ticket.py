import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    '''
    Generates a sorted list of length equal to the value of the parameter called
    quantity of unique random numbers within a specified range.
    '''

    if type(min) is not int or type(max) is not int or type(quantity) is not int:
        raise TypeError("All parameters must be integers.")
    if quantity > (max - min + 1):
        raise ValueError("Quantity exceeds the range of unique numbers available.")
    if min < 1:
        raise ValueError("Minimum value must be at least 1.")
    if max > 1000:
        raise ValueError("Maximum value must not exceed 1000.")
    if min > max:
        raise ValueError("Minimum value cannot be greater than maximum value.")

    res = set()

    while len(res) < quantity:
        num = random.randint(min, max)
        res.add(num)
    
    return sorted(list(res))

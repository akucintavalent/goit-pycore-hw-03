from datetime import datetime
import random
import re

def get_days_from_today(date: str) -> int:
    '''Returns the number of days from the given date to today.'''

    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days

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

def normalize_phone(phone_number: str) -> str:
    '''
    Normalizes a phone number by removing all non-numeric characters
    and ensuring it starts with the country code '+38' (for Ukraine).
    '''

    digits = re.sub(r'\D', '', phone_number)
    
    if len(digits) == 10:
        return '+38' + digits
    elif len(digits) == 12 and digits.startswith('38'):
        return '+' + digits
    else:
        raise ValueError("Invalid phone number format.")



if __name__ == "__main__":
    # input_date = input("Enter a date (YYYY-MM-DD): ")
    # days_difference = get_days_from_today(input_date)
    # print(f"Days from {input_date} to today: {days_difference}")

    # min_value = int(input("Enter minimum value for ticket numbers: "))
    # max_value = int(input("Enter maximum value for ticket numbers: "))
    # quantity_value = int(input("Enter quantity of ticket numbers: "))
    # ticket_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
    # print(f"Generated ticket numbers: {ticket_numbers}")

    phone_input = input("Enter a phone number: ")
    normalized_phone = normalize_phone(phone_input)
    print(f"Normalized phone number: {normalized_phone}")

    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

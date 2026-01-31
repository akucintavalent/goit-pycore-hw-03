from datetime import datetime
import random

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
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



if __name__ == "__main__":
    input_date = input("Enter a date (YYYY-MM-DD): ")
    days_difference = get_days_from_today(input_date)
    print(f"Days from {input_date} to today: {days_difference}")

    min_value = int(input("Enter minimum value for ticket numbers: "))
    max_value = int(input("Enter maximum value for ticket numbers: "))
    quantity_value = int(input("Enter quantity of ticket numbers: "))
    ticket_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
    print(f"Generated ticket numbers: {ticket_numbers}")

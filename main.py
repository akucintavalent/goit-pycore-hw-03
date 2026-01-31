from datetime import datetime, timedelta, date
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

def get_upcoming_birthdays(users: list[dict]) -> list[str]:
    '''
    Returns a sorted list of users who have birthdays in the next 7 days,
    adjusting for weekends by moving celebrations to the following Monday.
    '''

    def parse_date(date_str: str) -> date:
        return datetime.strptime(date_str, "%Y.%m.%d").date()

    today = datetime.today().date()
    upcoming_congratulation_dates = []
    for user in users:
        birthday = parse_date(user['birthday'])
        birthday_this_year = birthday.replace(year=today.year)
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:  # Saturday or Sunday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            upcoming_congratulation_dates.append({
                "name": user['name'],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return sorted(
        upcoming_congratulation_dates,
        key=lambda x: parse_date(x['congratulation_date'])
    )

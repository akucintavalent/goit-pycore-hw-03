from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''Returns the number of days from the given date to today.'''

    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days

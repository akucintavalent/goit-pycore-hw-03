from datetime import datetime, timedelta, date

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
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
        if days_until_birthday < 0:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
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

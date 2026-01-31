from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - date
    return delta.days





if __name__ == "__main__":
    input_date = input("Enter a date (YYYY-MM-DD): ")
    days_difference = get_days_from_today(input_date)
    print(f"Days from {input_date} to today: {days_difference}")

from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)

    return abs(d2 - d1).days


print(days_between_dates("2019-06-29", "2019-06-30"))
print(days_between_dates("2020-01-15", "2019-12-31"))
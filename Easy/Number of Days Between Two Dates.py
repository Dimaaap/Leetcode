import datetime


def days_between_dates(date1: str, date2: str):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    timestamp1 = date1.timestamp()
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    timestamp2 = date2.timestamp()
    diff = abs(timestamp1 - timestamp2)
    one_day = 24 * 60 * 60
    diff = int(diff / one_day)
    return diff


print(days_between_dates("2019-06-29", "2019-06-30"))
print(days_between_dates("2020-01-15", "2019-12-31"))

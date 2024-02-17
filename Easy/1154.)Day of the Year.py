def day_of_year(date: str):
    year, month, day = date.split("-")
    count_days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_number = int(month)
    counter = 0
    for i in range(month_number-1):
        counter += count_days[i]
    counter += int(day)
    return counter


def is_leap_year(year):
    year = int(year)
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


print(day_of_year("2019-01-09"))
print(day_of_year("2019-02-10"))
print(day_of_year("2003-03-01"))
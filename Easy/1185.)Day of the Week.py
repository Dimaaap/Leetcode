def day_of_the_week(day: int, month: int, year: int):
    prev_year = year - 1
    days = prev_year * 365 + prev_year // 4 - prev_year // 100 + prev_year // 400
    days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1])
    days += day

    if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        days += 1

    return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][days % 7]


print(day_of_the_week(31, 8, 2019))
print(day_of_the_week(18, 7, 1999))
print(day_of_the_week(21, 12, 1980))
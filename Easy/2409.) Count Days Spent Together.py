from datetime import date


def count_days_together(arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str):
    """
    Alice and Bob are traveling to Rome for separate business meetings.
    You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the
    dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to
    leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to
    the month and day of the date.
    Return the total number of days that Alice and Bob are in Rome together.
    You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number
    of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
    """
    def to_date(month_day: str):
        return date(2023, *map(int, month_day.split("-")))

    start = max(to_date(arrive_alice), to_date(arrive_bob))
    end = min(to_date(leave_alice), to_date(leave_bob))
    return max((end - start).days + 1, 0)


print(count_days_together("08-15", "08-18", "08-16", "08-19"))  # => 3
print(count_days_together("10-01", "10-31", "11-01", "12-31"))  # => 0

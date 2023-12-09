from datetime import datetime


def have_conflict(event1: list[str], event2: list[str]):
    """
    You are given two arrays of strings that represent two inclusive events that happened on the same day,
    event1 and event2, where:
        event1 = [startTime1, endTime1] and
        event2 = [startTime2, endTime2].
    Event times are valid 24 hours format in the form of HH:MM.
    A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
    Return true if there is a conflict between two events. Otherwise, return false.
    """

    def get_time(time_value: str):
        base_date = datetime(2023, 9, 12)
        time_object = datetime.combine(base_date, datetime.strptime(time_value, "%H:%M").time())
        return time_object

    max_start = max(get_time(event1[0]), get_time(event2[0]))
    min_end = min(get_time(event1[1]), get_time(event2[1]))
    return max_start <= min_end


print(have_conflict(["01:15", "02:00"], ["02:00", "03:00"]))
print(have_conflict(["01:00", "02:00"], ["01:20", "03:00"]))
print(have_conflict(["10:00", "11:00"], ["14:00", "15:00"]))

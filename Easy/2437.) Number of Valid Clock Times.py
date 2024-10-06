import re


def count_time(time: str) -> int:

    """
    You are given a string of length 5 called time, representing the current time on a digital clock in the format
    "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

    In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a
    digit from 0 to 9.

    Return an integer answer, the number of valid clock times that can be created by replacing every ?
    with a digit from 0 to 9.
    """

    pattern = time.replace("?", ".")
    return(sum(
        re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
        for hour in range(24)
        for minute in range(60)
    ))


print(count_time("?5:00"))
print(count_time("0?:0?"))
print(count_time("??:??"))
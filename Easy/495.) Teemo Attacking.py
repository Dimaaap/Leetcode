def find_poisoned_duration(time_series: list[int], duration: int):
    """
    Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
    attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More
    formally, an attack at second t will mean Ashe is poisoned during
    the inclusive time interval [t, t + duration - 1]. If Teemo attacks
    again before the poison effect ends, the timer for it is reset, and the
    poison effect will end duration seconds after the new attack.
    You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes
    that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
    Return the total number of seconds that Ashe is poisoned.
    """
    total = 0
    l = len(time_series)
    for i in range(l):
        if i < l - 1:
            if time_series[i] + duration - 1 < time_series[i + 1]:
                total += duration
            else:
                total += time_series[i + 1] - time_series[i]
        else:
            total += duration
    return total


print(find_poisoned_duration([1, 4], 2))
print(find_poisoned_duration([1, 2], 2))
print(find_poisoned_duration([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))

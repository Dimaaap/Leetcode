def find_min_difference(time_points: list[str]) -> int:
    """
    Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes
    difference between any two time-points in the list.
    """

    minutes = []

    for time in time_points:
        hours, mins = map(int, time.split(":"))
        minutes.append(hours * 60 + mins)
    minutes.sort()

    min_diff = float("inf")

    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i - 1])
    wrap_around = 1440 - minutes[-1] + minutes[0]
    min_diff = min(min_diff, wrap_around)

    return min_diff



print(find_min_difference(["23:59", "00:00"]))
print(find_min_difference(["23:59", "00:00", "00:00"]))
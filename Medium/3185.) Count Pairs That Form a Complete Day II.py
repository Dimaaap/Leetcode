def count_complete_pairs(hours: list[int]) -> int:
    """
    Given an integer array hours representing times in hours, return an integer denoting the number of
    pairs i, j where i < j and hours[i] + hours[j] forms a complete day.
    A complete day is defined as a time duration that is an exact multiple of 24 hours.
    For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.
    :param hours:
    :return:
    """
    seen = {}
    counter = 0

    for hour in hours:
        reminder = hour % 24
        complement = (24 - reminder) % 24
        if complement in seen:
            counter += seen[complement]
        seen[reminder] = seen.get(reminder, 0) + 1
    return counter



print(count_complete_pairs([12, 12, 30, 24, 24]))


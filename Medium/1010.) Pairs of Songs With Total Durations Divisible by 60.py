def num_pairs_divisible_by_60(time: list[int]) -> int:
    """
    You are given a list of songs where the ith song has a duration of time[i] seconds.
    Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we
    want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
    """
    counter = 0

    for i in range(len(time)):
        for j in range(i + 1, len(time)):
            if (time[i] + time[j]) % 60 == 0:
                counter += 1
    return counter


print(num_pairs_divisible_by_60([30, 20, 150, 100, 40]))
print(num_pairs_divisible_by_60([60, 60, 60]))
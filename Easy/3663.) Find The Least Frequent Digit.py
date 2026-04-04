from collections import defaultdict


def get_least_frequent_digit(n: int) -> int:
    """
    Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits
    have the same frequency, choose the smallest digit.
    Return the chosen digit as an integer.
    The frequency of a digit x is the number of times it appears in the decimal representation of n.
    """
    n = str(n)
    counter = defaultdict(int)

    for num in n:
        counter[int(num)] += 1

    sorted_counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    return sorted_counter[0][0]

print(get_least_frequent_digit(1553322))
print(get_least_frequent_digit(723344511))
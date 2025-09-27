from collections import defaultdict


def largest_values_from_labels(value: list[int], labels: list[int], num_wanted: int, use_limit: int) -> int:
    """
    You are given n item's value and label as two integer arrays values and labels. You are also given two
    integers numWanted and useLimit.
    Your task is to find a subset of items with the maximum sum of their values such that:

    The number of items is at most numWanted.
    The number of items with the same label is at most useLimit.
    Return the maximum sum.
    """
    seen = {}

    for v, l in zip(value, labels):
        if v in seen:
            seen[v].append(l)
        else:
            seen[v] = [l]
    seen = dict(sorted(seen.items(), key=lambda x: x[0], reverse=True))
    res = counter = 0
    seen_values = defaultdict(int)
    while counter < num_wanted:
        for k, v in seen.items():
            for count in v:
                if count not in seen_values or seen_values[count] < use_limit:
                    res += k
                    counter += 1
                    seen_values[count] += 1
                if counter == num_wanted:
                    break
            if counter == num_wanted:
                break
            else:
                continue
        else:
            break
    return res


print(largest_values_from_labels([5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1))
print(largest_values_from_labels([5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2))
print(largest_values_from_labels([9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1))
print(largest_values_from_labels([3, 2, 3, 2, 1], [1, 0, 2, 2, 1], 2, 1))
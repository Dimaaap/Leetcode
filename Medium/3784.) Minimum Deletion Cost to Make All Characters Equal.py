def min_cost(s: str, cost: list[int]) -> int:
    """
    You are given a string s of length n and an integer array cost of the same length, where cost[i] is the cost to
    delete the ith character of s.
    You may delete any number of characters from s (possibly none), such that the resulting string is non-empty and
    of equal characters.
    Return an integer denoting the minimum total deletion cost required.
    """

    char_cost = {}
    for ch, c in zip(s, cost):
        if ch in char_cost:
            char_cost[ch] += c
        else:
            char_cost[ch] = c
    costs = sorted(char_cost.values())
    if len(costs) == 1:
        return 0
    return sum(costs[:-1])


print(min_cost("aabaac", [1, 2, 3, 4, 1, 10]))
print(min_cost("abc", [10, 5, 8]))
print(min_cost("zzzzz", [67, 67, 67, 67, 67]))
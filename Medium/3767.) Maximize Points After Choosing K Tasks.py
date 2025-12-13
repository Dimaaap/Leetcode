def max_points(technique1: list[int], technique2: list[int], k: int) -> int:
    """
    You are given two integer arrays, technique1 and technique2, each of length n, where n represents the number
    of tasks to complete.

    If the ith task is completed using technique 1, you earn technique1[i] points.
    If it is completed using technique 2, you earn technique2[i] points.
    You are also given an integer k, representing the minimum number of tasks that must be completed using technique 1.

    You must complete at least k tasks using technique 1 (they do not need to be the first k tasks).

    The remaining tasks may be completed using either technique.

    Return an integer denoting the maximum total points you can earn.

    """
    n = len(technique1)

    res = [[technique1[i], technique2[i]] for i in range(n)]
    res.sort(key=lambda s: (s[0] - s[1]), reverse=True)
    tot = 0
    for i in range(k):
        tot += res[i][0]
    for i in range(k, n):
        tot += max(res[i][0], res[i][1])
    return tot


print(max_points([5, 2, 10], [10, 3, 8], 2))
print(max_points([10, 20, 30], [5, 15, 25], 2))
print(max_points([112, 855], [723, 568], 0))

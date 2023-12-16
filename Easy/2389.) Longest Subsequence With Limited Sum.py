def answer_queries(nums: list[int], queries: list[int]):
    """
    You are given an integer array nums of length n, and an integer array queries of length m.
    Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take
     from nums such that the sum of its elements is less than or equal to queries[i].
    A subsequence is an array that can be derived from another array by deleting some or no elements
    without changing the order of the remaining elements.
    """
    nums.sort()
    res = []
    for q in queries:
        total = 0
        count = 0
        for num in nums:
            total += num
            count += 1
            if total > q:
                count -= 1
                break
        res.append(count)
    return res


print(answer_queries([4, 5, 2, 1], [3, 10, 21]))
print(answer_queries([2, 3, 4, 5], [1]))

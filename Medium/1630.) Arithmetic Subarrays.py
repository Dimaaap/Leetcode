def check_arithmetic_subarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    """
        A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference
        between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only
        if s[i+1] - s[i] == s[1] - s[0] for all valid i.

        You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m
        range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

        Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]],
        nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
    """
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        subarray = nums[l[i]:r[j] + 1]
        subarray = sorted(subarray)[::-1]
        first_num = subarray[0] - subarray[1]
        for k in range(1, len(subarray) - 1):
            if subarray[k] - subarray[k + 1] != first_num:
                res.append(False)
                break
        else:
            res.append(True)
        i += 1
        j += 1
    return res


print(check_arithmetic_subarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))
print(check_arithmetic_subarrays([-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                 [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]))

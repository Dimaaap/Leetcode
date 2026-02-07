def find_missing_elements(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums consisting of unique integers.
    Originally, nums contained every integer within a certain range. However, some integers might
    have gone missing from the array.
    The smallest and largest integers of the original range are still present in nums.
    Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.
    """

    range_start, range_end = min(nums), max(nums)

    range_list = list(range(range_start, range_end + 1))
    res = []
    for i in range_list:
        if i not in nums:
            res.append(i)
    return res


print(find_missing_elements([1, 4, 2, 5]))
print(find_missing_elements([7, 8, 6, 9]))
print(find_missing_elements([5, 1]))
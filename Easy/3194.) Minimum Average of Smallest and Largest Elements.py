def minimum_average(nums: list[int]) -> float:
    """
    You have an array of floating point numbers averages which is initially empty. You are given an array
     nums of n integers where n is even.

    You repeat the following procedure n / 2 times:

    Remove the smallest element, minElement, and the largest element maxElement, from nums.
    Add (minElement + maxElement) / 2 to averages.
    Return the minimum element in averages.
    """
    nums = sorted(nums)
    min_avg = max(nums)
    while nums:
        min_el, max_el = nums.pop(0), nums.pop(-1)
        min_avg = min(min_avg, (min_el + max_el) / 2)
    return min_avg


print(minimum_average([7, 8, 3, 4, 15, 13, 4, 1]))
print(minimum_average([1, 2, 3, 7, 8, 9]))
print(minimum_average([1, 9, 8, 3, 10, 5]))
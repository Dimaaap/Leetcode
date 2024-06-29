def minimum_average(nums: list[int]) -> float:
    """
    You have an array of floating point numbers averages which is initially empty. You are given an array
     nums of n integers where n is even.

    You repeat the following procedure n / 2 times:

    Remove the smallest element, minElement, and the largest element maxElement, from nums.
    Add (minElement + maxElement) / 2 to averages.
    Return the minimum element in averages.
    """
    sorted_nums = sorted(nums)
    averages = []
    while sorted_nums:
        min_el, max_el = sorted_nums[0], sorted_nums[-1]
        avg = (min_el + max_el) / 2
        averages.append(avg)
        sorted_nums.pop()
        sorted_nums.pop(0)
    return min(averages)



print(minimum_average([7, 8, 3, 4, 15, 13, 4, 1]))
print(minimum_average([1, 2, 3, 7, 8, 9]))
print(minimum_average([1, 9, 8, 3, 10, 5]))
def minimum_deletions(nums: list[int]) -> int:
    """
    You are given a 0-indexed array of distinct integers nums.
    There is an element in nums that has the lowest value and an element that has the highest value.
    We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
    A deletion is defined as either removing an element from the front of the array or removing an element from
    the back of the array.
    Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
    """
    min_el, max_el = min(nums), max(nums)
    min_index, max_index = nums.index(min_el), nums.index(max_el)
    left, right = min(min_index, max_index), max(min_index, max_index)

    return min(right + 1, len(nums) - left, left + 1+(len(nums) - right))

print(minimum_deletions([2, 10, 7, 5, 4, 1, 8, 6]))
print(minimum_deletions([0, -4, 19, 1, 8, -2, -3, 5]))
print(minimum_deletions([101]))
print(minimum_deletions([42, -75]))

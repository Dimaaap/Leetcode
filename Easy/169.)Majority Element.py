def majority_element(nums: list[int]):
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    n = len(nums) / 2
    set_nums = set(nums)
    for i in set_nums:
        if nums.count(i) > n:
            return i

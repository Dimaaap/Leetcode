def is_trionic(nums: list[int]) -> bool:
    """
    You are given an integer array nums of length n.
    An array is trionic if there exist indices 0 < p < q < n − 1 such that:
        nums[0...p] is strictly increasing,
        nums[p...q] is strictly decreasing,
        nums[q...n − 1] is strictly increasing.
    Return true if nums is trionic, otherwise return false.
    """

    i = 1
    res = []
    increase_index = None
    decrease_index = None
    while i < len(nums) - 1:
        if not increase_index:
            if nums[i] <= nums[i - 1]:
                return False
        if nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
            return False
        if nums[i - 1] < nums[i] > nums[i + 1]:
            increase_index = i
            res.append(i)
        if nums[i - 1] > nums[i] < nums[i + 1] and increase_index:
            decrease_index = i
            res.append(i)
        i += 1
    if len(res) == 2 and increase_index and decrease_index:
        return True
    return False


print(is_trionic([1, 3, 5, 4, 2, 6]))
print(is_trionic([2, 1, 3]))
print(is_trionic([4, 1, 5, 2, 3]))
print(is_trionic([3, 3, 8, 1, 4, 6]))
print(is_trionic([5, 6, 4, 6, 8, 8, 7]))
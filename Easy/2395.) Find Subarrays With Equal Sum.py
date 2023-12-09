def find_subarray(nums: list[int]):
    """
    Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum.
    Note that the two subarrays must begin at different indices.
    Return true if these subarrays exist, and false otherwise.
    A subarray is a contiguous non-empty sequence of elements within an array.
    """
    visited_sum = set()
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum in visited_sum:
            return True
        else:
            visited_sum.add(current_sum)
    return False


print(find_subarray([4, 2, 4]))  # => True
print(find_subarray([1, 2, 3, 4, 5]))  # => False
print(find_subarray([0, 0, 0]))  # => True

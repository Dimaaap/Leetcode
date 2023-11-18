def find_the_array_conc_val(nums: list[int]):
    """
    You are given a 0-indexed integer array nums.
    The concatenation of two numbers is the number formed by concatenating their numerals.
        For example, the concatenation of 15, 49 is 1549.
    The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
        If there exists more than one number in nums, pick the first element and last element in nums respectively
        and add the value of their concatenation to the concatenation value of nums, then delete the first
        and last element from nums.
        If one element exists, add its value to the concatenation value of nums, then delete it.
    Return the concatenation value of the nums.
    """
    concat_val = 0
    while len(nums) >= 2:
        concat = str(nums[0]) + str(nums[-1])
        concat_val += int(concat)
        nums = nums[1:-1]
    concat_val += nums[0] if nums else 0
    return concat_val


print(find_the_array_conc_val([7, 52, 2, 4]))
print(find_the_array_conc_val([5, 14, 13, 8, 12]))


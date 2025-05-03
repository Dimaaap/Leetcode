def sum_of_good_numbers(nums: list[int], k: int) -> int:
    """
    Given an array of integers nums and an integer k, an element nums[i] is considered good if it
    is strictly greater than the elements at indices i - k and i + k (if those indices exist).
    If neither of these indices exists, nums[i] is still considered good.

    Return the sum of all the good elements in the array.
    """
    i = result = 0
    while i < len(nums):
        prev_element = None
        next_element = None
        if i - k > -1:
            prev_element = nums[i - k]
        if i + k <= len(nums) - 1:
            next_element = nums[i + k]
        if prev_element:
            if next_element:
                res = nums[i] if prev_element < nums[i] > next_element else 0
                result += res
            else:
                res = nums[i] if nums[i] > prev_element else 0
                result += res
        elif next_element:
            res = nums[i] if nums[i] > next_element else 0
            result += res
        i += 1
    return result


print(sum_of_good_numbers([1, 3, 2, 1, 5, 4], 2))
print(sum_of_good_numbers([2, 1], 1))
print(sum_of_good_numbers([17, 20], 1))

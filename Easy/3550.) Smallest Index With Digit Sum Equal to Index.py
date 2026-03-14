def smallest_index(nums: list[int]) -> int:
    """
    You are given an integer array nums.
    Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
    If no such index exists, return -1.
    """

    for index, num in enumerate(nums):
        str_num = str(num)
        digit_sum = sum(int(char) for char in str_num)

        if digit_sum == index:
            return index
    return -1


print(smallest_index([1, 3, 2]))
print(smallest_index([1, 10, 11]))
print(smallest_index([1, 2, 3]))
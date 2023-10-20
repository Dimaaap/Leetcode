def sum_of_unique(nums: list[int]):
    """
    You are given an integer array nums. The unique elements of an array
    are the elements that appear exactly once in the array.
    Return the sum of all the unique elements of nums.
    """
    ans = 0
    for num in nums:
        if nums.count(num) == 1:
            ans += num
    return ans


print(sum_of_unique([1, 2, 3, 2]))
print(sum_of_unique([1, 1, 1, 1]))
print(sum_of_unique([1, 2, 3, 4, 5]))
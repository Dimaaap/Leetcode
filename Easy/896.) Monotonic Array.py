def is_monotonic(nums: list[int]):
    if sorted(nums) == nums or sorted(nums)[::-1] == nums:
        return True
    return False


print(is_monotonic([1, 2, 2, 3]))
print(is_monotonic([6, 5, 4, 4]))
print(is_monotonic([1, 3, 2]))
def is_array_special(nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        first_parity = nums[i] % 2
        second_parity = nums[i + 1] % 2
        if bool(first_parity) == bool(second_parity):
            return False
    return True


print(is_array_special([1]))
print(is_array_special([2, 1, 4]))
print(is_array_special([4, 3, 1, 6]))
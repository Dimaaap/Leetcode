def get_final_state(nums: list[int], k: int, multiplier: int) -> list[int]:
    i = 0
    while i < k:
        min_num = nums.index(min(nums))
        nums[min_num] = nums[min_num] * multiplier
        i += 1
    return nums


print(get_final_state([2, 1, 3, 5, 6], 5, 2))
print(get_final_state([1, 2], 3, 4))
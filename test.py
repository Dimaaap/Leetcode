def is_possible_to_split(nums: list[int]):
    first_arr = []
    second_arr = []
    for i in range(len(nums)):
        if nums[i] not in first_arr and len(first_arr) < len(nums) // 2:
            first_arr.append(nums[i])
        else:
            second_arr.append(nums[i])
    if len(set(second_arr)) == len(second_arr):
        return True
    return False


# print(is_possible_to_split([1, 1, 2, 2, 3, 4]))
# print(is_possible_to_split([1, 1, 1, 1]))
print(is_possible_to_split([2, 10, 2, 7, 8, 9, 7, 6, 6, 9]))
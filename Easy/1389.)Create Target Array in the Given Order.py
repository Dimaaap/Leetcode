def create_target_array(nums: list[int], index: list[int]):
    result_array = []
    for i in range(len(index)):
        result_array.insert(index[i], nums[i])
    return result_array


print(create_target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
print(create_target_array([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))

def shuffle(nums: list[int], n: int):
    left_array, right_array = nums[:n], nums[n:]
    final_array = []
    for i, j in zip(left_array, right_array):
        final_array.append(i)
        final_array.append(j)
    return final_array


print(shuffle([2, 5, 1, 3, 4, 7], 3))
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
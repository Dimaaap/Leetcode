def num_identical_pairs(nums: list[int]):
    counter = 0
    for index, element in enumerate(nums):
        for j in nums[index+1:]:
            if element == j:
                counter += 1
    return counter


print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
print(num_identical_pairs([1, 1, 1, 1]))
print(num_identical_pairs([1, 2, 3]))

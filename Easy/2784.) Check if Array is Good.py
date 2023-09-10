def is_good(nums: list[int]):
    template_list = list(range(1, len(set(nums))+1)) + [len(set(nums))]
    return sorted(nums) == template_list


print(is_good([2, 1, 3]))
print(is_good([1, 3, 3, 2]))
print(is_good([1, 1]))
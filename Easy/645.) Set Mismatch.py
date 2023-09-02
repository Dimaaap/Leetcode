def find_error_nums(nums: list[int]):
    range_list = set(list(range(1, len(nums)+1)))
    set_nums = set(nums)
    result_list = []
    result_list.extend(set([i for i in nums if nums.count(i) > 1]))
    for i in range_list:
        if i not in set_nums:
            result_list.append(i)
    return result_list


print(find_error_nums([1, 2, 2, 4]))
print(find_error_nums([1, 1]))


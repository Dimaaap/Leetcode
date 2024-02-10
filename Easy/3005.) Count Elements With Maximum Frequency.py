def max_frequency_elements(nums: list[int]):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    counter = 0
    sorted_count_dict = sorted(count_dict.items(), key=lambda x: x[1])[::-1]
    max_count = max(count_dict.values())
    for k, v in sorted_count_dict:
        if v == max_count:
            counter += v
        else:
            break
    return counter


print(max_frequency_elements([1, 2, 2, 3, 1, 4]))
print(max_frequency_elements([1, 2, 3, 4, 5]))

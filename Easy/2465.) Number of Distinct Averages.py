def distinct_averages(nums: list[int]):
    averages = set()
    while nums:
        min_num, max_num = min(nums), max(nums)
        avg = (min_num + max_num) / 2
        averages.add(avg)
        nums.remove(min_num)
        nums.remove(max_num)
    return len(averages)


print(distinct_averages([4, 1, 4, 0, 3, 5]))
print(distinct_averages([1, 100]))

def number_of_pairs(nums: list[int]):
    cache = {}
    pairs = 0
    for num in nums:
        if num not in cache:
            cache[num] = 1
        else:
            cache[num] += 1
        if cache[num] % 2 == 0:
            pairs += 1
    return [pairs, abs(len(nums) - pairs * 2)]


print(number_of_pairs([1, 3, 2, 1, 3, 2, 2]))
print(number_of_pairs([1, 1]))

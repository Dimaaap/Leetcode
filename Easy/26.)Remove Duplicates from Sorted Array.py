def remove_duplicates(nums: list[int]):
    hash_table = {}
    counter = 0
    deleted_el = []
    i = 0
    while i < len(nums):
        if nums[i] not in hash_table:
            counter += 1
            hash_table[nums[i]] = 1
            i += 1
        else:
            del nums[i]
            deleted_el.append("_")
    return counter, nums + deleted_el


print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

def remove_element(nums: list[int], val: int):
    counter = 0
    i = 0
    deleted_el = []
    while i < len(nums):
        if nums[i] == val:
            deleted_el.append("_")
            del nums[i]
        else:
            counter += 1
            i += 1
    nums += deleted_el
    return counter


print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
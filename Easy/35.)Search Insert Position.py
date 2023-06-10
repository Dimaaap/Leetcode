def search_insert(nums: list[int], target: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return low


print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))
print(search_insert([1, 3, 5, 6], 0))
print(search_insert([1, 3], 1))

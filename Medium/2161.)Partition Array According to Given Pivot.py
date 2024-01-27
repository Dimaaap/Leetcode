def pivot_array(nums: list[int], pivot: int):
    n = len(nums)
    ans = []
    count = 0
    for i in range(n):
        if nums[i] < pivot:
            ans.append(nums[i])
        elif nums[i] == pivot:
            count += 1
    for i in range(count):
        ans.append(pivot)
    for i in range(n):
        if nums[i] > pivot:
            ans.append(nums[i])
    return ans


print(pivot_array([9, 12, 5, 10, 15, 3, 10], 10))
print(pivot_array([-3, 4, 3, 2], 2))
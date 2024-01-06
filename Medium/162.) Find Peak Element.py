def find_peak_element(nums: list[int]):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and nums[mid] < nums[mid-1]:
            high = mid-1
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            return mid


print(find_peak_element([1, 2, 3, 1]))
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))
print(find_peak_element([1]))
print(find_peak_element([1, 2]))
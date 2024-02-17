def peak_index_in_mountain_array(arr: list[int]):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] > arr[mid]:
            right = mid
        else:
            left = mid


print(peak_index_in_mountain_array([0, 1, 0]))
print(peak_index_in_mountain_array([0, 2, 1, 0]))
print(peak_index_in_mountain_array([0, 10, 5, 2]))
print(peak_index_in_mountain_array([3, 9, 8, 6, 4]))
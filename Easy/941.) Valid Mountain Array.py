def valid_mountain_array(arr: list[int]):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left+1] > arr[left] and arr[right-1] > arr[right]:
            left += 1
            right -= 1
        elif arr[right-1] > arr[right]:
            right -= 1
        elif arr[left+1] > arr[left]:
            left += 1
        else:
            return False
    return True


print(valid_mountain_array([2, 1]))
print(valid_mountain_array([3, 5, 5]))
print(valid_mountain_array([0, 3, 2, 1]))
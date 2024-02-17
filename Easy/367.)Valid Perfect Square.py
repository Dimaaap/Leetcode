def is_perfect_square(num: int):
    if num == 1:
        return True
    left, right = 1, num // 2
    while left <= right:
        mid = int((left + right) / 2)
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(is_perfect_square(16))
print(is_perfect_square(14))
print(is_perfect_square(1))

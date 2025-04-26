def can_partition(num, target, start):
    if target == 0:
        return True
    if start >= len(num):
        return False

    for end in range(start + 1, len(num) + 1):
        part = int(num[start:end])
        if part > target:
            break
        if can_partition(num, target - part, end):
            return True
    return False


def punishment_number(n):
    total = 0
    for i in range(1, n + 1):
        square_str = str(i ** 2)
        if can_partition(square_str, i, 0):
            total += int(square_str)
    return total


print(punishment_number(10))
print(punishment_number(37))
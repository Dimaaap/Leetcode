def two_sum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1

    while i < j:
        res = numbers[i] + numbers[j]
        if res > target:
            j -= 1
        if res < target:
            i += 1
        if res == target:
            return [i + 1, j + 1]
    return []


print(two_sum([1, 2, 3, 4], 3))
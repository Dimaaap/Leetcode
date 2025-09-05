def count_complete_day_pair(numbers: list[int]) -> int:
    counter = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if i != j:
                if (numbers[i] + numbers[j]) % 24 == 0:
                    counter += 1
    return counter


print(count_complete_day_pair([12, 12, 30, 24, 24]))
print(count_complete_day_pair([72, 24, 24, 3]))
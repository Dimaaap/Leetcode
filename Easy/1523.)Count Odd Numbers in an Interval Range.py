def count_odds(low: int, high: int):
    counter = 0
    for i in range(low, high + 1):
        if i % 2 != 0:
            counter += 1
    return counter


print(count_odds(3, 7))
print(count_odds(8, 10))
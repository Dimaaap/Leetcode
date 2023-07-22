def kids_with_candies(candies: list[int], extra_candies: int):
    max_candie = max(candies)
    results_list = []
    for candie in candies:
        if candie + extra_candies >= max_candie:
            results_list.append(True)
        else:
            results_list.append(False)
    return results_list


print(kids_with_candies([2, 3, 5, 1, 3], 3))
print(kids_with_candies([4, 2, 1, 1, 2], 1))
print(kids_with_candies([12, 1, 2], 10))
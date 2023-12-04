def time_required_to_buy(tickets: list[int], k: int):
    counter = 0
    i = 0
    while tickets[k] != 0:
        if tickets[i] != 0:
            tickets[i] -= 1
            counter += 1
        i = (i + 1) % len(tickets)
    return counter


print(time_required_to_buy([2, 3, 2], 2))
print(time_required_to_buy([5, 1, 1, 1], 0))

def maximum_wealth(accounts: list[list[int]]):
    initial_sum = sum(accounts[0])
    for account in accounts[1:]:
        if sum(account) > initial_sum:
            initial_sum = sum(account)
    return initial_sum


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
def buy_choco(prices: list[int], money: int):
    prices.sort()
    rest_money = money - sum(prices[:2])
    return rest_money if rest_money >= 0 else money


print(buy_choco([1, 2, 2], 3))
print(buy_choco([3, 2, 3], 3))

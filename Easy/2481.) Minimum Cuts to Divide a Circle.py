def number_of_cuts(n: int):
    if n == 1:
        return 0
    return n // 2 if n % 2 == 0 else n


print(number_of_cuts(4))
print(number_of_cuts(3))
print(number_of_cuts(1))

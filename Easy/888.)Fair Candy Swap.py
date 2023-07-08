def fair_candy_swap(alice_sizes: list[int], bob_sizes: list[int]):
    difference = (sum(alice_sizes) - sum(bob_sizes)) / 2
    a = set(alice_sizes)
    for candy in set(bob_sizes):
        if difference + candy in a:
            return [difference + candy, candy]


print(fair_candy_swap([1, 1], [2, 2]))
print(fair_candy_swap([1, 2], [2, 3]))
print(fair_candy_swap([2], [1, 3]))

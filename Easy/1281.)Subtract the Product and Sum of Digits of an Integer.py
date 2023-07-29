def subtract_product_and_sum(n: int):
    digit_sum, digit_product = 0, 1
    while n:
        n, rest = divmod(n, 10)
        digit_sum += rest
        digit_product *= rest
    return digit_product - digit_sum


print(subtract_product_and_sum(234))
print(subtract_product_and_sum(4421))
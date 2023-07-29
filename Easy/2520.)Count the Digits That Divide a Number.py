def count_digits(num: int):
    new_number = num
    counter = 0
    while num:
        num, rest = divmod(num, 10)
        if new_number % rest == 0:
            counter += 1
    return counter


print(count_digits(7))
print(count_digits(121))
print(count_digits(1248))
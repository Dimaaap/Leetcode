def add_digits(num: int) -> int:
    num_sum = 0
    while len(str(num)) > 1:
        num_sum = str(sum(int(i) for i in str(num)))
        num = num_sum
    return int(num_sum)


print(add_digits(38))
print(add_digits(0))
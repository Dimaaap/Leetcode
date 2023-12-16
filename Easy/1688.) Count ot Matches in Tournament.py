def number_of_matches(n: int):
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
            counter += n
        else:
            counter += 1
            n = (n - 1) / 2
            counter += n
    return int(counter)


print(number_of_matches(7))
print(number_of_matches(14))


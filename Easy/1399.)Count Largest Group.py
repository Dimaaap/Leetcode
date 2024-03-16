def count_largest_group(n: int):
    digits_count = {}
    for i in range(1, n+1):
        digits_sum = count_digits_sum(i)
        if digits_sum in digits_count:
            digits_count[digits_sum].append(i)
        else:
            digits_count[digits_sum] = [i]
    digits_count = sorted(digits_count.values(), key=lambda x: len(x))[::-1]
    counter = 0
    max_len = len(digits_count[0])
    for i in digits_count:
        if len(i) == max_len:
            counter += 1
    return counter

def count_digits_sum(n: int):
    return sum(int(i) for i in str(n))


print(count_largest_group(13))
print(count_largest_group(2))
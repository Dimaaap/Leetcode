def count_event(num: int):

    def helper(number: int):
        new_num = number
        digit_sum = 0
        while number:
            number, rest = divmod(number, 10)
            digit_sum += rest
        return digit_sum

    counter = 0
    for i in range(2, num + 1):
        if helper(i) % 2 == 0:
            counter += 1

    return counter


print(count_event(4))
print(count_event(30))
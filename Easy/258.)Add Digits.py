def add_digits(num: int):
    new_num = num
    while True:
        ans_num = 0
        num = new_num
        while num:
            num, rest = divmod(num, 10)
            ans_num += rest
        new_num = ans_num
        if new_num < 10:
            return new_num


print(add_digits(38))
print(add_digits(0))
def get_no_zero_integers(n: int):
    def check(num):
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
        return True

    for i in range(1, n):
        t = n - i
        if check(t) and check(i):
            return [i, t]


def check_contains_zero(s):
    return "0" in str(s)


print(get_no_zero_integers(2))
print(get_no_zero_integers(11))
print(get_no_zero_integers(1000))
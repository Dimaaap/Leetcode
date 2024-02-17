def is_power_of_four(n: int):
    if n == 1 or n == 4:
        return True
    while n >= 4:
        n /= 4
        if n == 4:
            return True
    return False


print(is_power_of_four(16))
print(is_power_of_four(5))
print(is_power_of_four(1))
print(is_power_of_four(4))
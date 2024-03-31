def check_perfect_number(num: int):
    ans = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            ans += i
    return ans == num


print(check_perfect_number(28))
print(check_perfect_number(7))
print(check_perfect_number(99999992))
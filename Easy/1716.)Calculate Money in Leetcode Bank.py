def total_money(n: int):
    prev_mon = ans = count = 0
    while n:
        count += 1
        ans += count + prev_mon
        if count == 7:
            prev_mon += 1
            count = 0
        n -= 1
    return ans


print(total_money(4))
print(total_money(10))
print(total_money(20))

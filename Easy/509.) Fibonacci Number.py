def fib(n: int):
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each
    number is the sum of the two preceding ones, starting from 0 and 1
    Given n, calculate F(n).
    """
    fib_nums = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        new_number = fib_nums[i-1] + fib_nums[i-2]
        fib_nums.append(new_number)
    return fib_nums[-1]


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(0))
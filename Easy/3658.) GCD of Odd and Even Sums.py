def gcd_of_odd_even_sums(n: int) -> int:
    """
    You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:
        sumOdd: the sum of the smallest n positive odd numbers.
        sumEven: the sum of the smallest n positive even numbers.
    Return the GCD of sumOdd and sumEven.
    """

    odd = [i for i in range(1, n * 2, 2)]
    even = [i for i in range(2, n * 2 + 1, 2)]

    sum_odd = sum(odd)
    sum_even = sum(even)

    def find_gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    return find_gcd(sum_odd, sum_even)


print(gcd_of_odd_even_sums(4))
print(gcd_of_odd_even_sums(5))
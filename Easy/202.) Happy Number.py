def is_happy(n: int):
    """
    Write an algorithm to determine if a number n is happy.
    Return true if n is a happy number, and false if not
    """
    visited = set()
    while n not in visited:
        visited.add(n)
        n = sum_of_square(n)
        if n == 1:
            return True

    return False


def sum_of_square(n) -> int:
    output = 0
    while n > 0:
        digits = n % 10
        digits = digits * digits
        output += digits
        n = n // 10
    return output


print(is_happy(19))

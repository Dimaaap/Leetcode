def add_binary(a: str, b: str):
    """
    Given two binary strings a and b, return their sum as a binary string.
    """
    a, b = list(a), list(b)
    carry = 0
    ans = ""
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        carry, remain = divmod(carry, 2)
        ans += str(remain)
    return ans[::-1]

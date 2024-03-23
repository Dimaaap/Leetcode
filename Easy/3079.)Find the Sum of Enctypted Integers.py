def sum_of_encrypted_int(nums: list[int]):
    """
    You are given an integer array nums containing positive integers.
    We define a function encrypt such that encrypt(x) replaces
    every digit in x with the largest digit in x. For example,
    encrypt(523) = 555 and encrypt(213) = 333.

    Return the sum of encrypted elements.
    """
    res = 0
    for num in nums:
        res += encrypt(num)
    return res

def encrypt(x: int):
    x = str(x)
    max_x = max(x)
    res = ""
    for _ in x:
        res += max_x
    return int(res)


print(sum_of_encrypted_int([1, 2, 3]))
print(sum_of_encrypted_int([10, 21, 31]))


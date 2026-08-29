def is_palindromic(s: str) -> bool:
    """
    You are given a string s consisting of lowercase English letters.
    Construct a binary string by replacing each character in s with the 8-bit binary representation of
    its ASCII value, including leading zeros, while preserving the original order of the characters.
    Return true if the resulting binary string is a palindrome. Otherwise, return false.
    """

    res = ""

    for char in s:
        number = ord(char)
        bin_num = f"{number:08b}"
        res += str(bin_num)

    return res == res[::-1]


print(is_palindromic("ff"))
print(is_palindromic("leet"))

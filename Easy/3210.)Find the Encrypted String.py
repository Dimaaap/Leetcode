def get_encrypted_string(s: str, k: int) -> str:

    """
    You are given a string s and an integer k. Encrypt the string using the following algorithm:

    For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).

    Return the encrypted string.
    """

    final_string = ""
    for char in range(len(s)):
        final_string += s[(char + k) % len(s)]
    return final_string


print(get_encrypted_string("dart", 3))
print(get_encrypted_string("aaa", 1))
print(get_encrypted_string("byd", 4))
print(get_encrypted_string("fvevzh", 10))
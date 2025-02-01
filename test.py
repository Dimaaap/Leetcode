from collections import deque


def get_encrypted_string(s: str, k: int) -> str:
    n = len(s)
    k = k % n
    result = ""
    for i in range(n):
        result += s[(i + k) % n]
    return result


print(get_encrypted_string("dart", 3))
print(get_encrypted_string("aaa", 1))

from collections import deque


def di_string_match(s: str) -> list[int]:
    """
    A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s
    of length n where:
        s[i] == 'I' if perm[i] < perm[i + 1], and
        s[i] == 'D' if perm[i] > perm[i + 1].
    Given a string s, reconstruct the permutation perm and return it. If there are multiple valid
    permutations perm, return any of them.
    """
    numbers = deque(range(0, len(s) + 1))
    res = []
    for char in s:
        if char == "I":
           res.append(numbers[0])
           numbers.popleft()
        else:
            res.append(numbers[-1])
            numbers.pop()
    res.append(numbers[-1])
    return res


print(di_string_match("IDID"))
print(di_string_match("III"))
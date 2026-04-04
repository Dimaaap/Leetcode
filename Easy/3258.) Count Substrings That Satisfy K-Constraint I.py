def count_k_constraint_substrings(s: str, k: int) -> int:
    """
    You are given a binary string s and an integer k.
    A binary string satisfies the k-constraint if either of the following conditions holds:

        The number of 0's in the string is at most k.
        The number of 1's in the string is at most k.
    Return an integer denoting the number of substrings of s that satisfy the k-constraint.
    """

    counter = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i: j + 1]
            if substr.count("1") <= k or substr.count("0") <= k:
                counter += 1
    return counter


print(count_k_constraint_substrings("10101", 1))
print(count_k_constraint_substrings("1010101", 2))
print(count_k_constraint_substrings("11111", 1))
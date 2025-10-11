def letter_case_permutation(s: str) -> list[str]:
    """
    Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

    Return a list of all possible strings we could create. Return the output in any order.
    """

    res = [""]

    for char in s:
        if char.isalpha():
            res = [r + char.lower() for r in res] + [r + char.upper() for r in res]
        else:
            res = [r + char for r in res]
    return res


print(letter_case_permutation("a1b2"))
print(letter_case_permutation("3z4"))
print(letter_case_permutation("Jw"))
print(letter_case_permutation("mQe"))
print(letter_case_permutation("Jrq"))
def next_greatest_letter(letters: list[str], target: str):
    """
    You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
    There are at least two different characters in letters.
    Return the smallest character in letters that is lexicographically greater than target.
    If such a character does not exist, return the first character in letters.
    """
    for i in letters:
        if i > target:
            return i
    return letters[0]


print(next_greatest_letter(["c", "f", "j"], "a"))
print(next_greatest_letter(["c", 'f', "j"], "c"))
print(next_greatest_letter(["x", "x", "y", "y"], "z"))
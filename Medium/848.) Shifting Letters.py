from string import ascii_lowercase


def shifting_letters(s: str, shifts: list[int]) -> str:
    """
    You are given a string s of lowercase English letters and an integer array shifts of the same length.

    Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
    Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

    Return the final string after all such shifts to s are applied.
    """
    new_s = list(s)
    for i in range(0, len(s)):
        count_letters = i + 1
        for j in range(0, count_letters):
            new_s[j] = shift(new_s[j], shifts[i])
    return "".join(new_s)


def shift(letter: str, count: int) -> str:
    letters = ascii_lowercase
    index = letters.index(letter)
    new_letter = (index + count) % len(letters)
    return letters[new_letter]


print(shifting_letters("abc", [3, 5, 9]))
print(shifting_letters("aaa", [1, 2, 3]))

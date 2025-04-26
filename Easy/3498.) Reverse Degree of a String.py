from string import ascii_lowercase

def reverse_degree(s: str) -> int:
    """
    Given a string s, calculate its reverse degree.
    The reverse degree is calculated as follows:
        For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
        with its position in the string (1-indexed).
        Sum these products for all characters in the string.
    Return the reverse degree of s.
    """
    numbers = tuple(range(1, 27))[::-1]
    reverse_alphabet = {letter: num for letter, num in zip(ascii_lowercase, numbers) }
    result = 0
    for index, letter in enumerate(s):
        product = (index + 1) * reverse_alphabet[letter]
        result += product
    return result


print(reverse_degree("abc"))
print(reverse_degree("zaza"))

from string import ascii_lowercase


def map_word_weights(words: list[str], weights: list[int]) -> str:
    """
    You are given an array of strings words, where each string represents a word containing lowercase English letters.
    You are also given an integer array weights of length 26, where weights[i] represents the weight of the ith
    lowercase English letter.
    The weight of a word is defined as the sum of the weights of its characters.

    For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse
    alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').
    Return a string formed by concatenating the mapped characters for all words in order.
    """
    letters = ascii_lowercase
    digits = list(range(0, 26))

    digit_letter = {}
    for digit, letter in zip(digits, letters[::-1]):
        digit_letter[digit] = letter

    weights_total = []

    for word in words:
        word_weight = 0
        for index, letter in enumerate(word):
            order = letters.index(letter)
            weight = weights[order]
            word_weight += weight
        mod_weight = word_weight % 26
        weights_total.append(mod_weight)
    res = ""
    for w in weights_total:
        res += digit_letter[w]
    return res


print(map_word_weights(["abcd", "def", "xyz"],
                       [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]))
print(map_word_weights(["a", "b", "c"],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(map_word_weights(["abcd"],
                       [7, 5, 3, 4, 3, 5, 4, 9, 4, 2, 2, 7, 10, 2, 5, 10, 6, 1, 2, 2, 4, 1, 3, 4, 4, 5]))
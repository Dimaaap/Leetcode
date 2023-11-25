from string import ascii_lowercase


def is_sum_equal(first_word: str, second_word: str, target_word: str):
    letters = tuple(ascii_lowercase[:10])
    digits = tuple(range(0, 10))
    letters_digits = {letter: digit for letter, digit in zip(letters, digits)}
    first_sum = ''
    second_sum = ''
    third_sum = ''
    for i in first_word:
        first_sum += str(letters_digits[i])
    for i in second_word:
        second_sum += str(letters_digits[i])
    for i in target_word:
        third_sum += str(letters_digits[i])
    return int(first_sum) + int(second_sum) == int(third_sum)


print(is_sum_equal("acb", "cba", "cdb"))
print(is_sum_equal("aaa", 'a', "aab"))
print(is_sum_equal("aaa", "a", "aaaa"))

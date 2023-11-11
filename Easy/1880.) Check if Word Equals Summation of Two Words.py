from string import ascii_lowercase


def is_sum_equal(first_word: str, second_word: str, target_word: str):
    letters = ascii_lowercase[:10]
    digits = tuple(range(10))
    let_dict = {letter: digit for letter, digit in zip(letters, digits)}
    first_count = second_count = 0
    for i in first_word


print(is_sum_equal("acb", "cba", "cdb"))
print(is_sum_equal("aaa", "a", "aab"))
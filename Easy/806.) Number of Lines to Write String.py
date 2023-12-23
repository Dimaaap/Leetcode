from string import ascii_lowercase


def number_of_lines(widths: list[int], s: str):
    letter_width = {l: w for l, w in zip(ascii_lowercase, widths)}
    count_lines = 1
    count_width = 0
    for i in s:
        if count_width + letter_width[i] > 100:
            count_lines += 1
            count_width = letter_width[i]
        else:
            count_width += letter_width[i]
    return [count_lines, count_width]


print(number_of_lines(
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "abcdefghijklmnopqrstuvwxyz"))
print(number_of_lines(
    [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "bbbcccdddaaa"))

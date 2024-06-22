def most_common_word(paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower().split()
    counter = {}
    for i in paragraph:
        i = i.rstrip(".").rstrip(",").rstrip("!")
        if i not in banned:
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1
    sorted_dict = sorted(counter.items(), key=lambda x: x[1])[::-1]
    return sorted_dict[0][0]


# print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.",
#                        ["hit"]))
# print(most_common_word("a.", []))
print(most_common_word("a, a, a, a, b,b,b,c, c", ["a"]))
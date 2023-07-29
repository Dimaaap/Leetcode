def most_words_found(sentences: list[str]):
    max_len = len(sentences[0].split())
    for sentence in sentences[1:]:
        split_sentence = sentence.split()
        if len(split_sentence) > max_len:
            max_len = len(split_sentence)
    return max_len


print(most_words_found(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(most_words_found(["please wait", "continue to fight", "continue to win"]))

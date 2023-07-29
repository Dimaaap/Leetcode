def to_goat_latin(sentence: str):
    vowel_strings = "aeiouAEIOU"
    result_list = []
    count_a = 1
    sentence = sentence.split()
    for word in sentence:
        if word[0] in vowel_strings:
            result_list.append(word + "ma" + "a" * count_a)
        else:
            result_list.append(word[1:] + word[0] + "ma" + "a" * count_a)
        count_a += 1
    return result_list


print(to_goat_latin("I speak Goat Latin"))
print(to_goat_latin("The quick brown fox jumped over the lazy dog"))

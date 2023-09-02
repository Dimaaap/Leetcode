def uncommon_from_sentences(s1: str, s2: str):
    overall_list = s1.split() + s2.split()
    counter_dict = {}
    for word in overall_list:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1
    overall_list = []
    for k, v in counter_dict.items():
        if v == 1:
            overall_list.append(k)
    return overall_list


print(uncommon_from_sentences("this apple is sweet", "this apple is sour"))
print(uncommon_from_sentences("apple apple", "banana"))
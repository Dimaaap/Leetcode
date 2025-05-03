def max_difference(s: str) -> int:
    counter = {}
    for i in s:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    odd_freq = {char: count for char, count in counter.items() if count % 2 != 0}
    odd_freq = sorted(odd_freq.items(), key=lambda item: item[1])
    even_freq = {char: count for char, count in counter.items() if count % 2 == 0}
    even_freq = sorted(even_freq.items(), key=lambda item: item[1])
    highest_odd = odd_freq[-1][-1]
    smallest_even = even_freq[0][-1]
    return highest_odd - smallest_even


print(max_difference("aaaaabbc"))
print(max_difference("abcabcab"))
print(max_difference("mmsmsym"))
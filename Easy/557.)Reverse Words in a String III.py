def reverse_words(s: str):
    s = s.split()
    return ' '.join([i[::-1] for i in s])


print(reverse_words("Let`s take LeetCode contest"))

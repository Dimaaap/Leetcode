def sort_sentence(s: str):
    s = s.split()
    s = sorted(s, key=lambda i: int(i[-1]))
    s = [i[:-1] for i in s]
    return ' '.join(s)


print(sort_sentence("is2 sentence4 This1 a3"))
print(sort_sentence("Myself2 Me1 I4 and3"))

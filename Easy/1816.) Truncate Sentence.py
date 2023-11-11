def truncate_sentence(s: str, k: int):
    s = s.split()[:k]
    return ' '.join(s)


print(truncate_sentence("Hello how are you Contestant", 4))
print(truncate_sentence("What is the solution to this problem", 4))
print(truncate_sentence("chopper is not a tanuki", 5))
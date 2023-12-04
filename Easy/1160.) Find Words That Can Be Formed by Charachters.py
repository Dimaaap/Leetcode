def count_characters(words: list[str], chars: str):
    chars = list(chars)
    counter = 0
    for i in words:
        if set(i).issubset(chars):
            counter += len(i)
    return counter


print(count_characters(["cat", "bt", "hat", "tree"], "attach"))
print(count_characters(["hello", "world", "leetcode"], "welldonehoneyr"))


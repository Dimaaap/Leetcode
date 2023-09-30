def check_almost_equivalent(word1: str, word2: str):
    check = set(word1 + word2)
    for i in check:
        if abs(word1.count(i) - word2.count(i)) >= 4:
            return False
    return True


print(check_almost_equivalent("aaaa", "bccb"))
print(check_almost_equivalent("abcdeef", "abaacc"))
print(check_almost_equivalent("cccddabba", "babababab"))
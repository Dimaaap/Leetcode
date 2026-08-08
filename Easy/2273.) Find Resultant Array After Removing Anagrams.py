def remove_anagrams(words: list[str]) -> list[str]:
    """
    You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

    In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams,
    and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies
    the conditions.

    Return words after performing all operations. It can be shown that selecting the indices for each operation in
    any arbitrary order will lead to the same result.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the
    original letters exactly once. For example, "dacb" is an anagram of "abdc".
    """

    i = 1
    while i < len(words):
        if is_anagram(words[i], words[i-1]):
            words = words[:i] + words[i + 1:]
        else:
            i += 1
    return words


def is_anagram(word1: str, word2: str) -> bool:
    all_letters = word1 + word2
    for i in all_letters:
        if i not in word2 or i not in word2 or word1.count(i) != word2.count(i):
            return False

    return True


print(remove_anagrams(["abba", "baba", "bbaa", "cd", "cd"]))
print(remove_anagrams(["a", "b", "c", "d", "e"]))
print(remove_anagrams(["abbb", "aaab"]))
print(remove_anagrams(["nelduncd","dcnndeul","uendlcnd","nluncedd","fozlsvr","osfvrlz","vozsrfl","dm","md","md","dm","md","dm","md","md","dm","dm","dm","dm","md","eatzkewuyx","a","wulzacir"]))
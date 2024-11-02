def report_spam(message: list[str], banned_words: list[str]):
    """
    You are given an array of strings message and an array of strings bannedWords.

    An array of words is considered spam if there are at least two words in it that exactly
    match any word in bannedWords.

    Return true if the array message is spam, and false otherwise.
    """
    count_spam = 0
    banned_words = set(banned_words)
    for i in message:
        if i in banned_words:
            count_spam += 1
    return count_spam >= 2


print(report_spam(["hello", "world", "leetcode"], ["world", "hello"]))
print(report_spam(["hello", "programming", "fun"], ["world", "programming", "leetcode"]))
print(report_spam(["l", "i", "l", "i", "l"], ["d", "a", "i", "v", "a"]))

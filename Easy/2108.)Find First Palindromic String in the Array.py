def first_palindrome(words: list[str]):
    for word in words:
        if helper(word):
            return word
    return ""


def helper(word):
    return word[::-1] == word


print(first_palindrome(["abc", "car", "ada", "racecar", "cool"]))
print(first_palindrome(["notapalindrome", "racecar"]))
print(first_palindrome(["def", "ghi"]))
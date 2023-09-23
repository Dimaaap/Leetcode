def longest_palindrome(s: str):
    """
    Given a string s, return the longest palindromic substring in s.
    """
    ans = ''
    for i in range(len(s)):
        l, r = i, i
        while 0 <= l <= r < len(s):
            if s[l] != s[r]:
                break
            if r - l + 1 > len(ans):
                ans = s[l: r + 1]
            l -= 1
            r += 1
        l, r = i, i + 1
        while 0 <= l <= r < len(s):
            if s[l] != s[r]:
                break
            if r - l + 1 > len(ans):
                ans = s[l: r + 1]
            l -= 1
            r += 1
    return ans


print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome("ac"))

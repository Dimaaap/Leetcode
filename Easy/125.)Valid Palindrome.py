def is_palindrome(s: str):
    ans = ""
    for i in s:
        if i.isalnum():
            ans += i.lower()
    return ans == ans[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

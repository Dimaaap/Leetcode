def reverse_only_letters(s: str):
    """
    Given a string s, reverse the string according to the following rules:

        All the characters that are not English letters remain in the same position.

        All the English letters (lowercase or uppercase) should be reversed.

    Return s after reversing it.
    """
    s = list(s)
    left, right = 0, len(s)-1
    while left < right:
        if s[left].isalpha() and s[right].isalpha():
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left].isalpha():
            right -= 1
        elif s[right].isalpha():
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s)


print(reverse_only_letters("ab-cd"))
print(reverse_only_letters("a-bC-dEf-ghIj"))
print(reverse_only_letters("Test1ng-Leet=code-Q!"))
print(reverse_only_letters("7_28]"))
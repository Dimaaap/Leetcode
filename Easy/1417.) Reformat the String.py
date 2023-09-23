def reformat(s: str):
    """
    You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase
    English letters and digits).
    You have to find a permutation of the string where no letter is followed by another
    letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
    Return the reformatted string or return an empty string if it is impossible to reformat the string.
    """
    letters, digits = [i for i in s if i.isalpha()], [i for i in s if i.isdigit()]
    if abs(len(letters) - len(digits)) > 1:
        return ""
    rv = []
    flag = len(letters) > len(digits)
    while letters or digits:
        rv.append(letters.pop() if flag else digits.pop())
        flag = not flag
    return "".join(rv)


print(reformat("a0b1c2"))
print(reformat("leetcode"))
print(reformat("1234567"))
print(reformat("covid2019"))
print(reformat("ab123"))

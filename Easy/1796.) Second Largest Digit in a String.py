def second_highest(s: str):
    """
    Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if
    it does not exist.
    An alphanumeric string is a string consisting of lowercase English letters and digits.
    """
    ans = {int(i) for i in s if i.isdigit()}
    ans = sorted(ans)
    if len(ans) >= 2:
        return ans[-2]
    return -1


print(second_highest("dfa12321afd"))
print(second_highest("abc1111"))

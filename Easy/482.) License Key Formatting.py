def license_key_formatting(s: str, k: int):
    """
    You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
    The string is separated into n + 1 groups by n dashes. You are also given an integer k.
    We want to reformat the string s such that each group contains exactly k characters, except for the first group,
    which could be shorter than k but still must contain at least one character. Furthermore,
    there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
    Return the reformatted license key.
    """
    s = ''.join(s.split('-'))
    ans = []
    stack = []
    for i in range(len(s) - 1, -1, -1):
        if len(stack) >= k:
            ans.append(stack[::-1])
            stack = [s[i].upper()]
        else:
            stack.append(s[i].upper())
    if stack:
        ans.append(stack[::-1])
    output = ""
    for i in ans[::-1]:
        output += ''.join(i)
        output += "-"
    return output.strip("-")


print(license_key_formatting("5F3Z-2e-9-w", 4))
print(license_key_formatting("2-5g-3-J", 2))

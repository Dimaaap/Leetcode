def maximum_value(strs: list[str]):
    """
    The value of an alphanumeric string can be defined as:
        The numeric representation of the string in base 10, if it comprises of digits only.
        The length of the string, otherwise.
    Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
    """
    ans = 0
    for word in strs:
        if all(i.isdigit() for i in word):
            ans = max(ans, int(word))
        else:
            ans = max(ans, len(word))
    return ans


print(maximum_value(["alic3", "bob", "3", "4", "0000"]))
print(maximum_value(["1", "01", "001", "0001"]))
def divisor_substring(num: int, k: int) -> int:
    """
    The k-beauty of an integer num is defined as the number of substrings of num when it is read as a
    string that meet the following conditions:

        It has a length of k.
        It is a divisor of num.

    Given integers num and k, return the k-beauty of num.
    Note:
        Leading zeros are allowed.
        0 is not a divisor of any value.
    A substring is a contiguous sequence of characters in a string.
    """

    str_num = str(num)
    counter = 0

    for i in range(len(str_num)):
        substring = str_num[i:i+k]

        if int(substring) == 0:
            continue

        if len(substring) == k:
            substring = int(substring)
            if num % substring == 0:
                counter += 1
    return counter


print(divisor_substring(240, 2))
print(divisor_substring(430043, 2))



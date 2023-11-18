def digit_count(num: str):
    """
    You are given a 0-indexed string num of length n consisting of digits.
    Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num,
    otherwise return false.
    """
    for index, element in enumerate(num):
        if num.count(str(index)) != int(element):
            return False
    return True


print(digit_count("1210"))
print(digit_count("038"))
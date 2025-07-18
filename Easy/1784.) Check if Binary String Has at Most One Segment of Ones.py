def check_ones_segment(s: str) -> bool:
    """
    Given a binary string s without leading zeros, return true if s
    contains at most one contiguous segment of ones. Otherwise, return false.0
    """
    ones_indexes = [i for i in range(len(s)) if s[i] == "1"]
    for i in range(len(ones_indexes)-1, 0, -1):
        if ones_indexes[i] - ones_indexes[i - 1] != 1:
            return False
    return True


print(check_ones_segment("1001"))
print(check_ones_segment("110"))
print(check_ones_segment("10"))
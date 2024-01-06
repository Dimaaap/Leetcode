def find_array(pref: list[int]):
    """
    You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
        pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
    Note that ^ denotes the bitwise-xor operation.
    It can be proven that the answer is unique.
    """
    for i in range(len(pref) - 1, 0, -1):
        pref[i] = (pref[i] ^ pref[i-1])
    return pref


print(find_array([5, 2, 0, 3, 1]))
print(find_array([13]))
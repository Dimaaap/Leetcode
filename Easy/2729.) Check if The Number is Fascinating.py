def is_fascinating(n: int):
    """
    You are given an integer n that consists of exactly 3 digits.
    We call the number n fascinating if, after the following modification, the resulting number
     contains all the digits from 1 to 9 exactly once and does not contain any 0's:
    Concatenate n with the numbers 2 * n and 3 * n.
    Return true if n is fascinating, or false otherwise.
    Concatenating two numbers means joining them together. For example, the concatenation
    of 121 and 371 is 121371.
    """
    new_n = str(n) + str(n * 2) + str(n * 3)
    new_n_set = {i for i in new_n if i != "0"}
    digits = list(range(1, 10))
    return len(new_n_set) == len(digits) and len(new_n) == len(new_n_set)


print(is_fascinating(192))
print(is_fascinating(100))
print(is_fascinating(267))
print(is_fascinating(783))
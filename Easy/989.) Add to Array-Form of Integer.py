def add_to_array_form(num: list[int], k: int):
    """
    The array-form of an integer num is an array representing its digits in left to right order.
    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
    """
    res = ""
    for i in num:
        res += str(i)
    ans = str(int(res) + k)
    list_ans = [int(i) for i in ans]
    return list_ans


print(add_to_array_form([1, 2, 0, 0], 34))
print(add_to_array_form([2, 7, 4], 181))
print(add_to_array_form([2, 1, 5], 806))
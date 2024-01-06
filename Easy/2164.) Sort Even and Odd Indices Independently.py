from itertools import zip_longest


def sort_even_odd(nums: list[int]):
    even = []
    odd = []
    for index, element in enumerate(nums):
        if index % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    even.sort()
    odd = sorted(odd)[::-1]
    ans = []
    for e, o in zip_longest(even, odd):
        if e:
            ans.append(e)
        if o:
            ans.append(o)
    return ans


print(sort_even_odd([4, 1, 2, 3]))
print(sort_even_odd([2, 1]))
print(sort_even_odd([5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21]))

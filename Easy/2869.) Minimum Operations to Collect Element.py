def min_operations(nums: list[int], k: int):
    """
    You are given an array nums of positive integers and an integer k.
    In one operation, you can remove the last element of the array and add it to your collection.
    Return the minimum number of operations needed to collect elements 1, 2, ..., k.
    """
    compare_set = set(range(1, k + 1))
    ans = set()
    counter = 0
    for i in reversed(nums):
        if i in compare_set:
            ans.add(i)
        counter += 1
        if ans == compare_set:
            return counter


print(min_operations([3, 1, 5, 4, 2], 2))
print(min_operations([3, 1, 5, 4, 2], 5))
print(min_operations([3, 2, 5, 3, 1], 3))
print(min_operations([3, 1, 5, 4, 2], 2))

def kth_largest_number(nums: list[str], k: int) -> str:
    nums = sorted(nums, key=lambda i: int(i))[::-1]
    return str(nums[k - 1])


print(kth_largest_number(["3", "6", "7", "10"], 4))
print(kth_largest_number(["2", "21", "12", "1"], 3))
print(kth_largest_number(["0", "0"], 2))
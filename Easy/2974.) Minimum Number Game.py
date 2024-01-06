def number_game(nums: list[int]):
    ans = []
    while nums:
        alice = min(nums)
        nums.remove(alice)
        bob = min(nums)
        nums.remove(bob)
        ans.extend((bob, alice))
    return ans


print(number_game([5, 4, 2, 3]))
print(number_game([2, 5]))
def arithmetic_triplets(nums: list[int], diff: int):
    """
    You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
    A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
        i < j < k,
        nums[j] - nums[i] == diff, and
        nums[k] - nums[j] == diff.
    Return the number of unique arithmetic triplets.
    """
    seen = {}
    ans = []
    for i in range(len(nums)):
        if nums[i] - diff in seen and nums[i] - diff * 2 in seen:
            ans.append((i, seen[nums[i] - diff], seen[nums[i]-diff * 2]))
            seen[nums[i]] = i
        else:
            seen[nums[i]] = i
    return len(ans)


print(arithmetic_triplets([0, 1, 4, 6, 7, 10], 3))
print(arithmetic_triplets([4, 5, 6, 7, 8, 9], 2))
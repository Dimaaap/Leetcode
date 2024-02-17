def tribonacci(n: int):
    first_nums = [0, 1, 1]
    for i in range(3, n+1):
        first_nums.append(first_nums[i-1] + first_nums[i-2] + first_nums[i-3])
    return first_nums[n]


print(tribonacci(4))
print(tribonacci(25))
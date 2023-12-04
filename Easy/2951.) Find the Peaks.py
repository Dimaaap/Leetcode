def find_peaks(mountain: list[int]):
    ans = []
    for i in range(1, len(mountain)-1):
        if mountain[i-1] < mountain[i] > mountain[i+1]:
            ans.append(i)
    return ans


print(find_peaks([2, 4, 4]))
print(find_peaks([1, 4, 3, 8, 5]))

from collections import Counter


def maximum_length_substring(s: str):
    ans = k = 0
    freq = Counter()
    for i, ch in enumerate(s):
        freq[ch] += 1
        while freq[ch] == 3:
            freq[s[k]] -= 1
            k += 1
        ans = max(ans, i - k + 1)
    return ans
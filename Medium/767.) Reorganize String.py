from collections import defaultdict
import heapq


def reorganize_string(s: str) -> str:
    """
    Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
    Return any possible rearrangement of s or return "" if not possible.
    """
    counter = defaultdict(int)

    for i in s:
        counter[i] += 1
    n = len(s)

    if max(counter.values()) > (n + 1) // 2:
        return ""

    heap = [(-count, char) for char, count in counter.items()]
    heapq.heapify(heap)
    result = []
    prev_count = 0
    prev_char = ""

    while heap:
        count, char = heapq.heappop(heap)
        result.append(char)

        count += 1

        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))
        prev_count = count
        prev_char = char

    return "".join(result)


print(reorganize_string("aab"))
print(reorganize_string("aaab"))
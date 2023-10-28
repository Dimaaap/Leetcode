def last_visited_integer(words: list[str]):
    """
    Given a 0-indexed array of strings words where words[i] is either a positive integer represented as a string or
    the string "prev".Start iterating from the beginning of the array; for every "prev" string seen in words,
    find the last visited integer in words which is defined as follows:
        Let k be the number of consecutive "prev" strings seen so far (containing the current string).
        Let nums be the 0-indexed array of integers seen so far and nums_reverse be the reverse of nums,
        then the integer at (k - 1)th index of nums_reverse will be the last visited integer for this "prev".
    If k is greater than the total visited integers, then the last visited integer will be -1.
    Return an integer array containing the last visited integers.
    """
    k, li, ans = 0, [], []
    for i in words:
        if i == "prev":
            k += 1
            if k > len(li):
                ans.append(-1)
            else:
                ans.append(li[-k])
        else:
            k = 0
            li.append(int(i))
    return ans


print(last_visited_integer(["1", "2", "prev", "prev", "prev"]))
print(last_visited_integer(["1", "prev", "2", "prev", "prev"]))

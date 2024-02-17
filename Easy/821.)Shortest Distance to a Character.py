def shortest_to_char(s: str, c: str):
    indices_list = [index for index, char in enumerate(s) if char == c]
    ans = []
    for index, char in enumerate(s):
        if len(indices_list) > 1:
            ans.append(min(abs(i - index) for i in indices_list))
        else:
            ans.append(abs(indices_list[0] - index))
    return ans


print(shortest_to_char("loveleetcode", "e"))
print(shortest_to_char("aaab", "b"))
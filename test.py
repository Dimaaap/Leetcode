def longest_common_prefix(strs: list[str]):
    shortest = sorted(strs, key=lambda i: len(i))[0]
    while shortest:
        for j in strs:
            if not j.startswith(shortest):
                shortest = shortest[:-1]




print(longest_common_prefix(["flower", "flow", "flight"]))
def balanced_string_split(s: str):
    count_r = 0
    count_l = 0
    global_counter = 0
    for char in s:
        if char == "R":
            count_r += 1
        elif char == "L":
            count_l += 1
        if count_l == count_r and count_l != 0:
            global_counter += 1
            count_r = 0
            count_l = 0
    return global_counter


print(balanced_string_split("RLRRLLRLRL"))
print(balanced_string_split("RLRRRLLRLL"))
print(balanced_string_split("LLLLRRRR"))
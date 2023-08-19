def divide_string(s: str, k: int, fill: str):
    result_list = []
    counter = 0
    count_string = ""
    for char in s:
        if counter == k:
            result_list.append(count_string)
            count_string = char
            counter = 1
        else:
            count_string += char
            counter += 1
    if len(count_string) < k:
        count_string += fill * (k - len(count_string))
    result_list.append(count_string)
    return result_list


print(divide_string("abcdefghi", 3, "x"))
print(divide_string("abcdefghij", 3, "x"))
def is_same_after_reversals(num: int):
    list_num = list(str(num))
    first_reversal_num = int(''.join(num_reverse(list_num)))
    second_reversal_num = int(''.join(num_reverse(list(str(first_reversal_num)))))
    if second_reversal_num != num:
        return False
    return True


def num_reverse(num_list: list):
    i, j = 0, len(num_list) - 1
    while i <= j:
        num_list[i], num_list[j] = num_list[j], num_list[i]
        i += 1
        j -= 1
    return num_list


print(is_same_after_reversals(526))
print(is_same_after_reversals(1800))
print(is_same_after_reversals(0))

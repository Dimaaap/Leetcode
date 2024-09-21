def num_different_integers(word: str) -> int:
    digits_list = []
    digit_str = ""
    for i in word:
        if i.isdigit():
            digit_str += i
        else:
            if digit_str:
                digits_list.append(int(digit_str))
            digit_str = ""
    if digit_str:
        digits_list.append(int(digit_str))
    return len(set(digits_list))


print(num_different_integers("a123bc34d8ef34"))
print(num_different_integers("leet1234code234"))
print(num_different_integers("a1b01c001"))
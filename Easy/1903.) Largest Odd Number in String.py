def largest_odd_number(num: str):
    int_num = int(num)
    while int_num:
        if int_num % 2 != 0:
            return str(int_num)
        int_num, rest = divmod(int_num, 10)
    return ""


print(largest_odd_number("52"))
print(largest_odd_number("4206"))
print(largest_odd_number("35427"))
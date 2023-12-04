def are_numbers_ascending(s: str):
    s = s.split()
    digit_stack = []
    for i in s:
        if i.isdigit() and not digit_stack:
            digit_stack.append(int(i))
        elif i.isdigit() and int(i) <= digit_stack[-1]:
            return False
        elif i.isdigit():
            digit_stack.append(int(i))
    return True


print(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(are_numbers_ascending("hello world 5 x 5"))
print(are_numbers_ascending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

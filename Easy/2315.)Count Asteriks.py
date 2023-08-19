def count_asteriks(s: str):
    asteriks_counter = 0
    split_s = s.split("|")
    for char in range(0, len(split_s), 2):
        asteriks_counter += split_s[char].count("*")
    return asteriks_counter


print(count_asteriks("l|*e*et|c**o|*de|"))
print(count_asteriks("iamaprogrammer"))
print(count_asteriks("yo|uar|e**|b|e***au|tifu|l"))
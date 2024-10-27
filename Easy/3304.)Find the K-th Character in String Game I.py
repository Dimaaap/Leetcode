def kth_character(k: int):
    start_word = "a"
    while len(start_word) < k:
        gen_string = ""
        for i in start_word:
            if i != "z":
                next_char = chr(ord(i) + 1)
                gen_string += next_char
            else:
                gen_string += "a"
        start_word += gen_string
    return start_word[k - 1]


print(kth_character(5))
print(kth_character(10))

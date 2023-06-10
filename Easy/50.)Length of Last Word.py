def length_of_last_word(s: str):
    last_word = s.split()[-1]
    return len(last_word)


print(length_of_last_word("Hello World"))
print(length_of_last_word("    fly me      to moon    "))
print(length_of_last_word("luffy is still joyboy"))
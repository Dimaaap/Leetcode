def final_string(s: str):
    """
    Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses
     the string that you have written. Typing other characters works as expected.
    You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
    Return the final string that will be present on your laptop screen.
    """
    s = list(s)
    for index, char in enumerate(s):
        if char == "i":
            s[:index] = s[:index][::-1]
            s[index] = ""
    return ''.join(s)


print(final_string("string"))
print(final_string("poiinter"))

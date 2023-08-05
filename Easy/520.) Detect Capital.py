def detect_capital(word: str):
    if word == word.upper() or word == word.lower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False


print(detect_capital("USA"))
print(detect_capital("FlaG"))
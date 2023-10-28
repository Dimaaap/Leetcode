from string import ascii_lowercase


def unique_morse_representations(words: list[str]):
    """
    Given an array of strings words where each word can be written as a concatenation of the
    Morse code of each letter.
    Return the number of different transformations among all words we have.
    """
    morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    letters = ascii_lowercase
    letter_morse = {}
    for i, j in zip(morse_letters, letters):
        letter_morse[j] = i
    decoding_words = []
    for word in words:
        new_word = ""
        for i in word:
            new_word += letter_morse[i]
        decoding_words.append(new_word)
    return len(set(decoding_words))


print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
print(unique_morse_representations(["a"]))

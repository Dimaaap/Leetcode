def shortest_completing_word(license_plate: str, words: list[str]) -> str:
    """
    Given a string licensePlate and an array of strings words, find the shortest completing word in words.

    A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in
    licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate,
    then it must appear in the word the same number of times or more.

    For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
    Possible completing words are "abccdef", "caaacab", and "cbca".

    Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest
    completing words, return the first one that occurs in words.
    """
    letters = [i.lower() for i in license_plate if i.isalpha()]
    res = []

    for word in words:
        if all(l in word for l in letters):
            for letter in word.lower():

                if letter in letters and letters.count(letter) > 1 and word.count(letter) != letters.count(letter):
                    break
            else:
                res.append(word)
        else:
            continue

    return sorted(res, key=len)[0]

print(shortest_completing_word("1s3 PSt", ["step", "steps", "stripe", "stepple"]))
print(shortest_completing_word("1s3 456", ["looks", "pest", "stew", "show"]))
print(shortest_completing_word("Ah71752",
                               ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]))
print(shortest_completing_word("e490936", [
    "involve", "those", "else", "violence", "six", "positive", "product", "expect", "close", "couple"
]))
print(shortest_completing_word("a279711", ["scientist", "lot", "next", "treatment", "speak",
                                           "right", "hit", "avoid", "machine", "space"]))
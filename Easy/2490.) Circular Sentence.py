def is_circular_sentence(sentence: str) -> bool:
    is_circular = True
    sentence = sentence.split()
    if sentence[0][0] != sentence[-1][-1]:
        return False
    for i in range(len(sentence) - 1):
        if not(sentence[i][-1] == sentence[i + 1][0]):
            is_circular = False
    return is_circular


print(is_circular_sentence("leetcode exercises sound delightful"))
print(is_circular_sentence("eetcode"))
print(is_circular_sentence("Leetcode is cool"))
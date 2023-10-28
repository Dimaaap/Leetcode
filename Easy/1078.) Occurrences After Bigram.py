def find_occurrence(text: str, first: str, second: str):
    """
    Given two strings first and second, consider occurrences in some text of the form "first second third",
    where second comes immediately after first, and third comes immediately after second.
    Return an array of all the words third for each occurrence of "first second third".
    """
    ans = []
    text = text.split()
    for i in range(len(text)-2):
        if text[i] == first and text[i+1] == second:
            ans.append(text[i+2])
    return ans


print(find_occurrence("alice is a good girl she is a good student", "a", "good"))
print(find_occurrence("we will we will rock you", "we", "will"))

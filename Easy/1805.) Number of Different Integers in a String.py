def num_different_integers(word: str):
    """
    You are given a string word that consists of digits and lowercase English letters.
    You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123
    34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8",
    and "34".
    Return the number of different integers after performing the replacement operations on word.
    Two integers are considered different if their decimal representations without any leading zeros are different.
    """
    ans = ""
    for i in word:
        if i.isdigit():
            ans += i
        else:
            if ans and ans[-1] != " ":
                ans += " "
    digits_set = {int(i) for i in ans.split() if i != " "}
    return len(digits_set)


print(num_different_integers("a123bc34d8ef34"))
print(num_different_integers("leet1234code234"))
print(num_different_integers("a1b01c001"))
print(num_different_integers("a123bc34d8ef34"))



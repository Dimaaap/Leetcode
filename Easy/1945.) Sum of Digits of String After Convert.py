from string import ascii_lowercase


def get_lucky(s: str, k: int):
    letters = tuple(ascii_lowercase)
    numbers = tuple(range(1, 27))
    let_num = {}
    for letter, number in zip(letters, numbers):
        let_num[letter] = number
    ans_string = ""
    for char in s:
        ans_string += str(let_num[char])
    counter = 0
    while k > 0:
        list_ans = list(ans_string)
        counter = 0
        for i in list_ans:
            counter += int(i)
        ans_string = str(counter)
        k -= 1
    return counter


print(get_lucky("iiii", 1))
print(get_lucky("leetcode", 2))
print(get_lucky("zbax", 2))

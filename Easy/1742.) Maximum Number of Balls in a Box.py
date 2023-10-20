def count_balls(low_limit: int, high_limit: int):
    ball_range = list(range(low_limit, high_limit + 1))
    boxes = {}
    for i in ball_range:
        digits_sum = get_digits_sum(i)
        if digits_sum in boxes:
            boxes[digits_sum] += 1
        else:
            boxes[digits_sum] = 1
    return max(boxes.values())


def get_digits_sum(number: int):
    ans = 0
    while number:
        number, res = divmod(number, 10)
        ans += res
    return ans


print(count_balls(1, 10))
print(count_balls(5, 15))
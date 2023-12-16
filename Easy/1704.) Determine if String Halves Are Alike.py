def halves_are_alike(s: str):
    vowels = 'aeiouAEIOU'
    half_index = int(len(s) / 2)
    left, right = s[:half_index], s[half_index:]
    left_counter = 0
    right_counter = 0
    for i in left:
        if i in vowels:
            left_counter += 1
    for i in right:
        if i in vowels:
            right_counter += 1
    return left_counter == right_counter



print(halves_are_alike('book'))
print(halves_are_alike('textbook'))
print(halves_are_alike("AbCdEfGh"))
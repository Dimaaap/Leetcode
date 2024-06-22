def minimum_chairs(s: str):
    """
    You are given a string s. Simulate events at each second i:
        If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
        If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
    Return the minimum number of chairs needed so that a chair is available for every
    person who enters the waiting room given that it is initially empty.
    """
    counter = 0
    max_counter = 0
    for i in s:
        if i == "E":
            counter += 1
        else:
            counter -= 1
        max_counter = max(max_counter, counter)
    return max_counter


print(minimum_chairs("EEEEEEE"))
print(minimum_chairs("ELELEEL"))
print(minimum_chairs("ELEELEELLL"))
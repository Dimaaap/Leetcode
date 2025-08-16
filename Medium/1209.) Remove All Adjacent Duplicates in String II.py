def remove_duplicates(s: str, k: int) -> str:
    """
    You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal
    letters from s and removing them, causing the left and the right side of the deleted substring to concatenate
    together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It is guaranteed that the
    answer is unique.
    """

    stack = []

    for i in s:
        if stack and stack[-1][0] == i:
            stack[-1] = (i, stack[-1][1] + 1)
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append((i, 1))
    return "".join(i * count for i, count in stack)


print(remove_duplicates("abcd", 2))
print(remove_duplicates("deeedbbcccbdaa", 3))
print(remove_duplicates("pbbcggttciiippooaais", 2))
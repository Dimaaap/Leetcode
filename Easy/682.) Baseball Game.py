def cal_points(operations: list[str]) -> int:
    """
    You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you
    start with an empty record.
    You are given a list of strings operations, where operations[i] is the ith operation you must apply to the
    record and is one of the following:

    An integer x.
        Record a new score of x.
    '+'.
        Record a new score that is the sum of the previous two scores.
    'D'.
        Record a new score that is the double of the previous score.
    'C'.
        Invalidate the previous score, removing it from the record.

    Return the sum of all the scores on the record after applying all the operations.

    The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer
    and that all operations are valid.
    """

    stack = []

    for operation in operations:
        if len(operation) >= 2 and operation[0] == "-":
            stack.append(-int(operation[1:]))
            continue

        if operation.isdigit():
            stack.append(int(operation))
        elif operation == "+":
            prev_sum = stack[-1] + stack[-2]
            stack.append(prev_sum)
        elif operation == "D":
            prev_score = stack[-1] * 2
            stack.append(prev_score)
        else:
            stack.pop()
    return sum(stack)


print(cal_points(["5", "2", "C", "D", "+"]))
print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(cal_points(["1", "C"]))
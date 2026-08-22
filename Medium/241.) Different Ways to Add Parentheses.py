def diff_ways_to_compute(expression: str) -> list[int]:
    """
    Given a string expression of numbers and operators, return all possible results from computing all the different
    possible ways to group numbers and operators. You may return the answer in any order.

    The test cases are generated such that the output values fit in a 32-bit integer and the number of
    different results does not exceed 104.
    """
    results = []

    for i, char in enumerate(expression):
        if char in "+-*":
            left_results = diff_ways_to_compute(expression[:i])
            right_results = diff_ways_to_compute(expression[i + 1:])

            for left in left_results:
                for right in right_results:
                    if char == "+":
                        results.append(left + right)
                    elif char == "*":
                        results.append(left * right)
                    elif char == "-":
                        results.append(left - right)
    if not results:
        results.append(int(expression))

    return results


print(diff_ways_to_compute("2-1-1"))
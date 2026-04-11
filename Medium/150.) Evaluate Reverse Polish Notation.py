def evalRPN(tokens: list[str]) -> int:
    """
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
    Evaluate the expression. Return an integer that represents the value of the expression.
    Note that:
        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.
    """

    stack = []

    for token in tokens:
        if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
            stack.append(int(token))
        else:
            first_operand, second_operand = stack.pop(), stack.pop()
            result = eval(f"{second_operand} {token} {first_operand}")
            stack.append(int(result))
    return stack[0]


print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["4", "13", "5", "/", "+"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
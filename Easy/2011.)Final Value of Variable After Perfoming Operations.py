def final_value_after_operations(operations: list[str]):
    initial_value = 0
    for operation in operations:
        if "+" in operation:
            initial_value += 1
        else:
            initial_value -= 1
    return initial_value


print(final_value_after_operations(["--X", "X++", "X++"]))
print(final_value_after_operations(["++X", "++X", "X++"]))
print(final_value_after_operations(["X++", "X++", "--X", "X--"]))
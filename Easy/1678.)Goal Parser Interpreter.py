def interpret(command: str):
    matches_dict = {"()": "o", "(al)": "al", "G": "G"}
    result_string = ""
    for i in range(len(command) - 1):
        if command[i] != "G":

    return result_string


print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
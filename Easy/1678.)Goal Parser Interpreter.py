def interpret(command: str):
    return command.replace("()", "o").replace("(al)", "al")


print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))

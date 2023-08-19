def cal_points(operations: list[str]):
    result_array = []
    for operation in operations:
        if operation[-1].isdigit():
            result_array.append(int(operation))
        elif operation == "C":
            result_array.pop()
        elif operation == "D":
            adding_element = int(result_array[-1] * 2)
            result_array.append(adding_element)
        elif operation == "+":
            adding_element = int(result_array[-1]) + int(result_array[-2])
            result_array.append(adding_element)
    return sum(result_array)


print(cal_points(["5", "2", "C", "D", "+"]))
print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(cal_points(["1", "C"]))

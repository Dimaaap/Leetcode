def self_dividing_numbers(left: int, right: int):
    result_list = []
    for number in range(left, right + 1):
        new_number = number
        while number:
            number, rest = divmod(number, 10)
            if new_number % rest != 0:
                break
        result_list.append(new_number)
    return result_list


print(self_dividing_numbers(1, 22))

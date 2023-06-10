def roman_to_int(s: str):
    """
    Given a roman numeral, convert it to an integer.
    """
    convert_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                          'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                          'CD': 400, 'CM': 900}
    index = 0
    output = 0
    if s in convert_dictionary:
        return convert_dictionary[s]
    while index < len(s) - 1:
        if s[index: index+2] in convert_dictionary:
            output += convert_dictionary[s[index: index+2]]
            index += 2
        else:
            output += convert_dictionary[s[index]]
            index += 1
    if s[-2:] in convert_dictionary:
        pass
    else:
        output += convert_dictionary[s[-1]]
    return output


print(roman_to_int('III'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))
print(roman_to_int("MCMXCIV"))
print(roman_to_int("IX"))
print(roman_to_int("D"))
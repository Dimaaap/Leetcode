def convert_date_to_binary(date: str) -> str:
    """
    You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

    date can be written in its binary representation obtained by converting year, month, and day to their binary
    representations without any leading zeroes and writing them down in year-month-day format.

    Return the binary representation of date.
    """


    date_list = [int(i) for i in date.split("-")]
    converted_list = [bin(i).replace("0b", "") for i in date_list]
    return "-".join(converted_list)


print(convert_date_to_binary("2080-02-29"))
print(convert_date_to_binary("1900-01-01"))
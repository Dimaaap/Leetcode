def check_record(s: str):
    return s.count("A") < 2 and "LLL" not in s


print(check_record("PPALLP"))
print(check_record("PPALLL"))
def remove_trailing_zeros(num: str) -> str:
    num = num.rstrip("0")
    return num


print(remove_trailing_zeros("51230100"))
print(remove_trailing_zeros("123"))
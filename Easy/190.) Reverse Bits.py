def reverse_bits(n: int):
    binary = bin(n)
    reverse = binary[-1: 1: -1]
    reverse = reverse + (32 - len(reverse)) * "0"
    return int(reverse, 2)

print(reverse_bits(0o00000010100101000001111010011100))
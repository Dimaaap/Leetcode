def hamming_weight(n: int):
    return bin(n).count("1")


print(hamming_weight(0o00000000000000000000000000001011))

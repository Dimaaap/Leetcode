def generate_the_string(n: int) -> str:
    if n % 2 == 0:
        return "a" * (n - 1) + "b"
    else:
        return "a" * n

print(generate_the_string(4))
print(generate_the_string(2))
print(generate_the_string(7))
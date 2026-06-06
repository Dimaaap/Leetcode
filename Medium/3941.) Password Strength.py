from string import ascii_lowercase, ascii_uppercase


def password_strength(password: str) -> int:
    """
    You are given a string password.

    The strength of the password is calculated based on the following rules:

        1 point for each distinct lowercase letter ('a' to 'z').
        2 points for each distinct uppercase letter ('A' to 'Z').
        3 points for each distinct digit ('0' to '9').
        5 points for each distinct special character from the set "!@#$".
        Each character contributes at most once, even if it appears multiple times.

    Return an integer denoting the strength of the password.
    """

    counter = 0
    spec_chars = "!@#$"

    for char in set(password):
        if char in ascii_lowercase:
            counter += 1
        if char in ascii_uppercase:
            counter += 2
        if char.isdigit():
            counter += 3
        if char in spec_chars:
            counter += 5
    return counter


print(password_strength("aA1!"))
print(password_strength("bbB11#"))
print(password_strength("vqztn2Z"))
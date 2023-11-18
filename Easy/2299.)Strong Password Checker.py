def strong_password_checker(password: str):
    special_characters = "!@#$%^&*()-+"
    if len(password) < 8:
        return False
    if not any(i.islower() for i in password) or not any(i.isupper() for i in password):
        return False
    if not any(i in special_characters for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return False
    return True


print(strong_password_checker("IloveLe3tcode!"))
print(strong_password_checker("Me+You--IsMyDream"))
print(strong_password_checker("1aB!"))
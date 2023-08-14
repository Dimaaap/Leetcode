def is_long_pressed_name(name: str, typed: str):
    for i in name:
        if i not in typed or typed.count(i) < name.count(i):
            return False
    return True


print(is_long_pressed_name("alex", "aaleex"))
print(is_long_pressed_name("saeed", "sssaed"))
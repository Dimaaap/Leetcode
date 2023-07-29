def count_matches(items: list[list[str]], rule_key: str, rule_value: str):
    index_value_matches = {"type": 0, "color": 1, "name": 2}
    rule = index_value_matches[rule_key]
    counter = 0
    for item in items:
        if item[rule] == rule_value:
            counter += 1
    return counter


print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                    "color", "silver"))
print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                    "type", "phone"))

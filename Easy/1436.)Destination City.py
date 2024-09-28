def dest_city(paths: list[list[str]]) -> str:
    start_cities = set()
    end_cities = set()
    for start, end in paths:
        start_cities.add(start)
        end_cities.add(end)
    return "".join(end_cities - start_cities)


print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paolo"]]))
print(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]))
print(dest_city([["A", "Z"]]))
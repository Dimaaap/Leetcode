def count_points(rings: str):
    seen = {}
    for index, element in enumerate(rings):
        if element.isdigit():
            if element in seen:
                seen[element].add(rings[index - 1])
            else:
                seen[element] = {rings[index-1]}
    counter = 0
    for i in seen:
        if len(seen[i]) == 3:
            counter += 1
    return counter


print(count_points("B0B6G0R6R0R6G9"))
print(count_points("B0R0G0R9R0B0G0"))
print(count_points("G4"))
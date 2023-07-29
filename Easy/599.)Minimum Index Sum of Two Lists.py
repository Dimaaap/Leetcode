def find_restaurant(list1: list[str], list2: list[str]):
    min_index = 1000
    min_index_string = ''
    result_list = []
    common_strings = set(list1) & set(list2)
    if len(common_strings) == 1:
        return ''.join(common_strings)
    for element in common_strings:
        element_index = list1.index(element) + list2.index(element)
        if element_index < min_index:
            min_index = element_index
            min_index_string = element
        elif element_index == min_index:
            result_list = [min_index_string, commo]
    return min_index_string


print(find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                      ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(find_restaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
print(find_restaurant(["happy", "sad", "good"], ["sad", "happy", "good"]))

def sort_people(names: list[str], heights: list[int]):
    """
    You are given an array of strings names, and an array heights that consists of distinct positive integers.
    Both arrays are of length n.
    For each index i, names[i] and heights[i] denote the name and height of the ith person.
    Return names sorted in descending order by the people's heights.
    """
    name_height = {}
    for name, height in zip(names, heights):
        name_height[height] = name
    sort_heights = sorted(list(name_height.keys()))[::-1]
    ans = [name_height[height] for height in sort_heights]
    return ans


print(sort_people(["Mary", "John", "Emma"], [180, 165, 170]))
print(sort_people(["Alice", "Bob", "Bob"], [155, 180, 150]))

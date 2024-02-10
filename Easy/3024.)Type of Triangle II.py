def triangle_type(nums: list[int]):
    nums_set = set(nums)
    if len(nums_set) == 1:
        return "equilateral"
    elif len(nums_set) == 2:
        return "isosceles" if can_be_triangle(nums) else "none"
    if can_be_triangle(nums):
        return "scalene"
    return "none"


def can_be_triangle(sides: list[int]):
    max_el = max(sides)
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            cur_sum = sides[i] + sides[j]
            if cur_sum <= max_el:
                return False
    return True


print(triangle_type([3, 3, 3]))
print(triangle_type([3, 4, 5]))
print(triangle_type([8, 4, 2]))
print(triangle_type([5, 3, 8]))
print(triangle_type([8, 4, 4]))


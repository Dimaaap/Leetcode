def find_closest(x: int, y: int, z: int) -> int:
    """
    You are given three integers x, y, and z, representing the positions of three people on a number line:

        x is the position of Person 1.
        y is the position of Person 2.
        z is the position of Person 3, who does not move.
        Both Person 1 and Person 2 move toward Person 3 at the same speed.

    Determine which person reaches Person 3 first:

        Return 1 if Person 1 arrives first.
        Return 2 if Person 2 arrives first.
        Return 0 if both arrive at the same time.
    Return the result accordingly.


    """
    x_to_z = abs(z - x)
    y_to_z = abs(z - y)

    if x_to_z > y_to_z:
        return 2
    elif x_to_z < y_to_z:
        return 1
    return 0


print(find_closest(2, 7, 4))
print(find_closest(2, 5, 6))
print(find_closest(1, 5, 3))
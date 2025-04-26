def max_containers(n: int, w: int, max_weight: int) -> int:
    """
    You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can
    hold one container with a weight of exactly w.
    However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum
    weight capacity, maxWeight.
    Return the maximum number of containers that can be loaded onto the ship
    """
    return n * n if n * n <= max_weight // w else max_weight // w


print(max_containers(2, 3, 15))
print(max_containers(3, 5, 20))
print(max_containers(1, 4, 15))
print(max_containers(3, 4, 66))
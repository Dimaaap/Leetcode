def count_servers(grid: list[list[int]]) -> int:
    """
    You are given a map of a server center, represented as a m * n integer matrix grid,
    where 1 means that on that cell there is a server and 0 means that it is no server.
    Two servers are said to communicate if they are on the same row or on the same column.

    Return the number of servers that communicate with any other server.
    """
    m, n = len(grid), len(grid[0])
    servers_indexes = []
    counter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                servers_indexes.append((i, j))

    for row, col in servers_indexes:
        for i in servers_indexes:
            if (i[0] == row or i[1] == col) and i != (row, col):
                counter += 1
                break
    return counter


print(count_servers([[1, 0], [0, 1]]))
print(count_servers([[1, 0], [1, 1]]))
print(count_servers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))


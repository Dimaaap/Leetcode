def find_degrees(matrix: list[list[int]]) -> list[int]:
    """
    You are given a 2D integer array matrix of size n x n representing the adjacency matrix of an undirected graph
    with n vertices labeled from 0 to n - 1.
        matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
        matrix[i][j] = 0 indicates that there is no edge between vertices i and j.
    The degree of a vertex is the number of edges connected to it.
    Return an integer array ans of size n where ans[i] represents the degree of vertex i.
    """

    res = []

    for i in matrix:
        res.append(i.count(1))
    return res


print(find_degrees([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
print(find_degrees([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
print(find_degrees([[0]]))
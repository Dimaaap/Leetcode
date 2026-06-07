def min_deletion_size(strs: list[str]) -> int:
    """
    You are given an array of n strings strs, all of the same length.
    The strings can be arranged such that there is one on each line, making a grid.
    For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
    abc
    bce
    cae
    You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed),
    columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you
    would delete column 1.
    Return the number of columns that you will delete.
    """
    current_col = 0
    cols_count = len(strs[0])
    counter = 0

    while current_col < cols_count:
        current_chars = [str[current_col] for str in strs]
        if current_chars != sorted(current_chars):
            counter += 1
        current_col += 1

    return counter


print(min_deletion_size(["cba", "daf", "ghi"]))
print(min_deletion_size(["a", "b"]))
print(min_deletion_size(["zyx", "wvu", "tsr"]))
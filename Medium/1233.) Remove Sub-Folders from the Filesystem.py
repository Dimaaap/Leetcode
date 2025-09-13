def remove_sub_folders(folder: list[str]) -> list[str]:
    """
    Given a list of folders folder, return the folders after removing all sub-folders in those folders.
    You may return the answer in any order.
    If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j]
    must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not
    a sub-folder of "/a/b/c".
    The format of a path is one or more concatenated strings of the form: '/' followed by one or more
    lowercase English letters.
        For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
    """
    folder = sorted(folder)
    folders = []
    fold = 0
    while fold < len(folder):
        for j in folders:
            if folder[fold].startswith(f"{j}/"):
                folder.pop(fold)
                break
        else:
            folders.append(folder[fold])
            fold += 1
    return folder


print(remove_sub_folders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(remove_sub_folders(["/a", "/a/b/c", "/a/b/d"]))
print(remove_sub_folders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
print(remove_sub_folders(["/ah/al/am", "/ah/al"]))
from itertools import zip_longest


def compare_versions(version1: str, version2: str) -> int:
    """
    Given two version strings, version1 and version2, compare them. A version string consists of revisions separated
    by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
    To compare version strings, compare their revision values in left-to-right order. If one of the version strings
    has fewer revisions, treat the missing revision values as 0.
    Return the following:
        If version1 < version2, return -1.
        If version1 > version2, return 1.
        Otherwise, return 0.
    """

    version1 = version1.split(".")
    version2 = version2.split(".")

    for seg1, seg2 in zip_longest(version1, version2, fillvalue=0):
        seg1 = int(seg1)
        seg2 = int(seg2)

        if seg1 > seg2:
            return 1
        elif seg1 < seg2:
            return -1

    return 0


print(compare_versions("1.2", "1.10"))
print(compare_versions("1.01", "1.001"))
print(compare_versions("1.0", "1.0.0.0"))
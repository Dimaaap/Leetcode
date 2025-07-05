def merge_arrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    i = 0
    j = 0
    res = []
    more_list = None
    less_list = None

    if len(nums1) != len(nums2):
        more_list = nums1 if len(nums1) > len(nums2) else nums2
        less_list = nums2 if more_list == nums1 else nums1

    while i < len(nums1) and j < len(nums2):
        id_1, val_1 = nums1[i]
        id_2, val_2 = nums2[j]
        if id_1 == id_2:
            res.append([id_1, val_1 + val_2])
            i += 1
            j += 1
        elif id_1 > id_2:
            res.append([id_2, val_2])
            j += 1
        else:
            res.append([id_1, val_1])
            i += 1
    if more_list:
        diff = len(more_list) - len(less_list)
        res += more_list[-diff:]
    return res

# print(merge_arrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
# print(merge_arrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
print(merge_arrays([[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],
                    [757,875],[788,208],[932,695]],
                   [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],
                    [177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],
                    [420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],
                    [672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],
                    [935,253],[982,385]]))



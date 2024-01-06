from collections import defaultdict


def sort_the_students(score: list[list[int]], k: int):
    rows = len(score)
    cols = len(score[0])
    marks_list = []
    for i in range(rows):
        for j in range(cols):
            if j == k:
                marks_list.append(score[i][j])
    marks_list = sorted(marks_list)[::-1]
    m = 0
    for i in range(rows):
        if marks_list[m] == score[i][k]:
            score[m], score[i] = score[i], score[m]
            m += 1
    return score


def sort_the_students_second(score: list[list[int]], k: int):
    hashmap = defaultdict(list)
    refer = {}
    ans = []
    for i in range(len(score)):
        hashmap[i].append(score[i])
        refer[i] = score[i][k]
    sorted_ans = [k for k, v in sorted(refer.items(), key=lambda a: a[1], reverse=True)]
    for k in sorted_ans:
        ans += hashmap[k]
    return ans


print(sort_the_students([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2))
print(sort_the_students([[3, 4], [5, 6]], 0))
print(sort_the_students([[64766, 11978, 20502, 21365, 79611, 36797, 58431, 89540, 59373, 25955],
                         [23358, 84599, 4675, 20979, 76889, 34630, 64098, 23468, 71448, 17848],
                         [51305, 66104, 88468, 5333, 17233, 32521, 14087, 42738, 46669, 65662],
                         [93306, 92793, 54009, 9715, 24354, 24895, 20069, 93332, 73836, 64359]], 5))

print(sort_the_students_second([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2))
print(sort_the_students([[3, 4], [5, 6]], 0))
print(sort_the_students([[64766, 11978, 20502, 21365, 79611, 36797, 58431, 89540, 59373, 25955],
                         [23358, 84599, 4675, 20979, 76889, 34630, 64098, 23468, 71448, 17848],
                         [51305, 66104, 88468, 5333, 17233, 32521, 14087, 42738, 46669, 65662],
                         [93306, 92793, 54009, 9715, 24354, 24895, 20069, 93332, 73836, 64359]], 5))


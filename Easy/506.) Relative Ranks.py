def find_relative_ranks(score: list[int]):
    sorted_score = sorted(score)[::-1]
    result_dict = {}
    medals_list = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for i in range(len(sorted_score)):
        if i < 3:
            result_dict[sorted_score[i]] = medals_list[i]
        else:
            result_dict[sorted_score[i]] = str(i+1)
    final_list = []
    for i in score:
        if i in result_dict:
            final_list.append(result_dict[i])
    return final_list


print(find_relative_ranks([5, 4, 3, 2, 1]))
print(find_relative_ranks([10, 3, 8, 9, 4]))
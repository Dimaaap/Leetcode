def find_relative_ranks(score: list[int]):
    """
    You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
    All the scores are guaranteed to be unique.
    The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place
    athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e.,
    the xth place athlete's rank is "x").

    Return an array answer of size n where answer[i] is the rank of the ith athlete.
    """
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
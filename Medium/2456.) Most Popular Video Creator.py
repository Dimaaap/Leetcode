from collections import defaultdict


def most_popular_creator(creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
    """
    You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video
    on a platform was created by creators[i], has an id of ids[i], and has views[i] views.

    The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator
    with the highest popularity and the id of their most viewed video.

    If multiple creators have the highest popularity, find all of them.
    If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
    Note: It is possible for different videos to have the same id, meaning that ids do not uniquely
    identify a video. For example, two videos with the same ID are considered as distinct videos with their own
    viewcount.

    Return a 2D array of strings answer where answer[i] = [creatorsi, idi] means that creatorsi has the highest
    popularity and idi is the id of their most popular video. The answer can be returned in any order.
    """
    mapped_data = {}
    highest_popularity = 0

    for creator, id, view in zip(creators, ids, views):
        if not creator in mapped_data:
            mapped_data[creator] = [view, id, view]
        else:
            prev = mapped_data[creator]
            prev[0] += view
            if (prev[2] == view and prev[1] > id) or (prev[2] < view):
                prev[1] = id
            if prev[2] < view:
                prev[2] = view
        highest_popularity = max(highest_popularity, mapped_data[creator][0])

    result = []
    for creator, [view, id, id_value] in mapped_data.items():
        if view == highest_popularity:
            result.append([creator, id])
    return result




print(most_popular_creator(
    ["alice", "bob", "alice", "chris"],
        ["one", "two", "three", "four"],
      [5, 10, 5, 4])
)

print(most_popular_creator(
    ["alice", "alice", "alice"],
    ["a", "b", "c"],
    [1, 2, 2]
))
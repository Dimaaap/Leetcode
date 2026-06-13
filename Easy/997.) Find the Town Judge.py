from collections import defaultdict


def find_judge(n: int, trust: list[list[int]]) -> int:
    """
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly
    the town judge.
    If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person
    labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
    """

    people_who_trust = defaultdict(list)
    trust_people = defaultdict(list)

    for who_trust, trust_person in trust:
        people_who_trust[who_trust].append(trust_person)
        trust_people[trust_person].append(who_trust)
    people = list(range(1, n + 1))
    i = 1
    while i <= len(people):
        if i in people_who_trust.keys():
            i += 1
            continue
        if len(trust_people[i]) < len(people) - 1:
            i += 1
            continue
        return i
    return -1


print(find_judge(2, [[1, 2]]))
print(find_judge(3, [[1, 3], [2, 3]]))
print(find_judge(3, [[1, 3], [2, 3], [3, 1]]))
from collections import defaultdict

def subdomain_visits(cpdomains: list[str]):
    """
    A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com",
    at the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a
    domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

    A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep is
    the number of visits to the domain and d1.d2.d3 is the domain itself.

    For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that
    discuss.leetcode.com was visited 9001 times.

    Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each
    subdomain in the input. You may return the answer in any order.
    """
    domain_count = defaultdict(int)

    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)

        subdomains = domain.split(".")
        for i in range(len(subdomains)):
            subdomain = ".".join(subdomains[i:])
            domain_count[subdomain] += count
    result = [str(count) + " " + subdomain for subdomain, count in domain_count.items()]
    return result


print(subdomain_visits(["9001 discuss.leetcode.code"]))
print(subdomain_visits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
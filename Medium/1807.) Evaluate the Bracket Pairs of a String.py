import re


def evaluate(s: str, knowledge: list[list[str]]) -> str:
    """
    You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

    For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the
    keys "name" and "age".
    You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each
    knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

    You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains
    some key key, you will:

        Replace key and the bracket pair with the key's corresponding valuei.
        If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark
        "?" (without the quotation marks).
    Each key will appear at most once in your knowledge. There will not be any nested brackets in s.
    Return the resulting string after evaluating all of the bracket pairs.
    """
    knowledge_dict = {key: value for key, value in knowledge}

    def replace_match(match):
        key = match.group(1)
        return knowledge_dict.get(key, "?")

    result = re.sub(r"\((.*?)\)", replace_match, s)
    return result


print(evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(evaluate("hi(name)", [["a", "b"]]))
print(evaluate("(a)(a)(a)aaa", [["a", "yes"]]))
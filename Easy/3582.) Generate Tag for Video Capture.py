from string import ascii_lowercase


def generate_tag(caption: str) -> str:
    """
    You are given a string caption representing the caption for a video.
    The following actions must be performed in order to generate a valid tag for the video:
        Combine all words in the string into a single camelCase string prefixed with '#'. A camelCase string is one
        where the first letter of all words except the first one is capitalized. All characters after the first
        character in each word must be lowercase.
        Remove all characters that are not an English letter, except the first '#'
        Truncate the result to a maximum of 100 characters.

    Return the tag after performing the actions on caption.
    """
    letters = ascii_lowercase
    caption = caption.split()
    tag = ""
    for index, word in enumerate(caption):
        if index == 0:
            tag += word.lower()
        else:
            tag += word.capitalize()
    tag = "".join([char for char in tag if char.lower() in letters])
    return ("#" + tag)[:100]


print(generate_tag("Leetcode daily streak achieved"))
print(generate_tag("can I Go There"))
print(generate_tag("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"))
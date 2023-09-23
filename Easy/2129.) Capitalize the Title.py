def capitalize_title(title: str):
    split_title = title.split()
    for word in range(len(split_title)):
        if len(split_title[word]) <= 2:
            split_title[word] = split_title[word].lower()
        else:
            split_title[word] = split_title[word].title()
    return ' '.join(split_title)


print(capitalize_title("capiTalIze tHe titLe"))
print(capitalize_title("First leTTeR of EACH Word"))
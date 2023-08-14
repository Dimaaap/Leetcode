def can_be_typed_words(text: str, broken_letters: str):
    split_set = set(text.split())
    counter = 0
    for word in split_set:
        if all([i not in broken_letters for i in word]):
            counter += 1
    return counter


print(can_be_typed_words("hello world", "ad"))
print(can_be_typed_words("leet code", "lt"))
print(can_be_typed_words("leet code", "e"))
print(can_be_typed_words("veikxddtjgpixjrux srxiqrczp cxaldqsvsxpzn xrlxovsjy "
                         "ervh cdtxwnahcvj xazmhniydmzsseuhq htrsuiabtzcjglilehrpxqcadk "
                         "ynls r pjkiwtcmvldcr t urevy fjmeutye gjnyd wv fueploq eol "
                         "zofra xnwaxnwh lpckcgzfcslugpmu judahwebqnwtk gfttojiqcffstkcq "
                         "nfxbw ugnviyeincmuzoosfy kdazdudaztlnj rqg umaohfgtvk i "
                         "vfhdvuvbih falmmrke rv zsaqn oswdlfq eapt mnr swcoa jhmui "
                         "t vkm tumfqvj ehcycfgzxjkhxhdbymmwxy xnsxxerahbrr silb "
                         "rqmhfbyopev fstlsvpblocrvrheghvgiuqftknewskmhbk nchoj bo cxovzradanq "
                         "fofsrtmnytq brcixelmzvdxmm",
                         "wqchprenozi"))

def decode_message(key: str, message: str):
    mapping = {" ": " "}
    i = 97
    for k in key:
        if k not in mapping and k != ' ':
            mapping[k] = chr(i)
            i += 1
    return "".join(mapping[m] for m in message)


print(decode_message("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))

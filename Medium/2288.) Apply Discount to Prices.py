def discount_prices(sentence: str, discount: int) -> str:
    """
    A sentence is a string of single-space separated words where each word can contain digits,
    lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence
    of digits preceded by a dollar sign.

    For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
    You are given a string sentence representing a sentence and an integer discount. For each word representing a
    price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should
    be represented with exactly two decimal places.

    Return a string representing the modified sentence.

    Note that all prices will contain at most 10 digits.
    """
    sentence = sentence.split()
    for i in range(len(sentence)):
        if sentence[i].startswith("$") and len(sentence[i]) > 1 and all(j.isdigit() for j in sentence[i][1:]):
            price = int(sentence[i][1:])
            new_price = price * (1 - discount / 100)
            sentence[i] = f"${new_price:.2f}"
    return " ".join(sentence)


print(discount_prices("there are $1 $2 and 5$ candies in the shop", 50))
print(discount_prices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))
print(discount_prices("$76111 ab $6 $", 48))
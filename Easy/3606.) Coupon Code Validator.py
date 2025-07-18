def validate_coupons(code: list[str], business_line: list[str], is_active: list[bool]) -> list[str]:
    """
    You are given three arrays of length n that describe the properties of n coupons: code, businessLine,
     and isActive. The ith coupon has:

        code[i]: a string representing the coupon identifier.
        businessLine[i]: a string denoting the business category of the coupon.
        isActive[i]: a boolean indicating whether the coupon is currently active.

    A coupon is considered valid if all the following conditions hold:

        code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
        businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
        isActive[i] is true.
    Return an array of the codes of all valid coupons, sorted first by their businessLine in the order:
    "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order
    within each category.
    """
    code_active_business_line = [(c, bl, ia) for c, bl, ia in zip(code, business_line, is_active)]
    valid_categories = ["electronics", "grocery", "pharmacy", "restaurant"]
    valid = []
    for c, bl, ia in code_active_business_line:
        valid_title = all(i.isalnum() or i == "_" for i in c)
        if c and valid_title and ia and bl in valid_categories:
            valid.append((c, bl))
    valid = sorted(valid, key=lambda c: (c[1], c[0]))
    return [i[0] for i in valid]


print(validate_coupons(["SAVE20", "", "PHARMA5", "SAVE@20"],
                       ["restaurant", "grocery", "pharmacy", "restaurant"],
                       [True, True, True, True]))
print(validate_coupons(["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
                       ["grocery", "electronics", "invalid"],
                       [False, True, True]))

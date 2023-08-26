def count_seniors(details: list[str]):
    counter = 0
    for detail in details:
        if int(detail[11: 13]) > 60:
            counter += 1
    return counter


print(count_seniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
print(count_seniors(["1313579440F2036","2921522980M5644"]))
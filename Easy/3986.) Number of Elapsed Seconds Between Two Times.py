from datetime import datetime, date


def seconds_between_time(start_time: str, end_time: str) -> int:
    start_time, end_time = (datetime.strptime(start_time, "%H:%M:%S").time()
                            , datetime.strptime(end_time, "%H:%M:%S").time())
    today = date.today()
    st = datetime.combine(today, start_time)
    et = datetime.combine(today, end_time)

    diff = str(et - st).split(":")
    res = 0

    i = 0
    while i <= 2:
        match i:
            case 0:
                res += int(diff[0]) * 60 * 60
            case 1:
                res += int(diff[1]) * 60
            case 2:
                res += int(diff[2])
        i += 1
    return res


print(seconds_between_time("01:00:00", "01:00:25"))
print(seconds_between_time("12:34:56", "13:00:00"))
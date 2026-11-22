
def get_dates(year):
    f = 28
    if year % 4 == 0:
        f = 29
    months = [31, f, 31, 30, 30, 30, 31, 31, 30, 31, 30, 31]
    dates = []
    for x in range(len(months)):
        month = x + 1
        m = str(month)
        if month < 10:
            m = '0' + m

        for y in range(1,months[x] + 1):
            d = str(y)
            if y < 10:
                d = '0' + str(y)

            date = d+m + str(year)
            dates.append(date)
    return dates

datelist = get_dates(26)


total_dates = [datelist[299:]]
for x in range(27, 99):
    dates = get_dates(x)
    total_dates.extend(dates)


def check_repeat(date):
    date = [x for x in date]
    return len(set(date)) != len(date)

max_streak = 0
start = '180926'
end = '000000'

streak = 0

starts = []
for x in range(len(total_dates)):

    if check_repeat(total_dates[x]):
        streak += 1
    else:
        if streak > max_streak:
            max_streak = streak
            end = total_dates[x]
            start = total_dates[x - streak -1]
        streak = 0

print(max_streak, start , end)
#diep anh :)
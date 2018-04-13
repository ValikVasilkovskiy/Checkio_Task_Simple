import calendar
from datetime import datetime
def most_frequent_days(year):
    # norm python calendar 0 = monday
    dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',
        5: 'Saturday', 6: 'Sunday'}
    cal = calendar.Calendar()
    stack = []
    # 12 month in the year
    for i in range(1, 13):
        for j in cal.itermonthdates(year, i):
            string_data = str(j)
            # get month from 2019-01-01
            if int(string_data[5:7]) == i:
                stack.append(datetime.weekday(j))
    favorite_day_count, list_favorite_days = stack.count(0), []
    # 0 - 6 days of week, favorite_day_count start with 0 (stack.count(0))
    for i in range(1, 7):
        if stack.count(i) > favorite_day_count:
            favorite_day_count = stack.count(i)
    # all days of week 0 - 6
    for i in range(0, 7):
        if favorite_day_count == stack.count(i):
            list_favorite_days.append(dict[i])
    return list_favorite_days

# test
print(most_frequent_days(9999))
# mon == 0, sun == 6
day = 0
count = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        if month in (4, 6, 9, 11):
            span = 30
        elif month == 2:
            if year % 4 != 0:
                span = 28
            else:
                if year % 100 == 0 and year % 400 != 0:
                    span = 28
                else:
                    span = 29
        else:
            span = 31
        # Compute the date at the beginning of the next month.
        day = (day + span) % 7
        if year >= 1901 and day == 6:
            count += 1

print count

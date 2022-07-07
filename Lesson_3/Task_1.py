def check_date(day, month, year):
    enter = input().replace('.', ' ').split()

    for _ in enter:
        day = int(enter[0])
        month = int(enter[1])
        year = int(enter[2])

        if day <= 31 and day != 0 and month <= 12 and month != 0 and len(str(year)) == 4 and year != 0:
            return 'OK'
        else:
            return 'FAILED'


print(check_date(21, 2, 1993))

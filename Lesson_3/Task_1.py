import datetime

def check_date(d, m, y):
    input_data_user = input("Введите дату: ").split()
    for elem in input_data_user:
        d = int(elem[0:3].replace('.', ''))
        m = int(elem[3:6].replace('.', ''))
        y = int(elem[6:10].replace('.', ''))

    try:
        datetime.date(day=d, month=m, year=y)
        return 'OK'

    except Exception:
        return 'FAILED'

print(check_date(21, 2, 1993))
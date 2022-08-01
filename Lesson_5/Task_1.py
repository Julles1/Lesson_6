students_mark = {}

while True:
     comm = input('-Команда- ')

     if "add" in comm:
        students_append = input('-Данные студента- ').split()
        name = students_append[0]
        sname = students_append[1]
        students_mark[name, sname] = []
        print("OK")

     if "all" in comm:
         count = 0
         for k, v in students_mark.items():
             if v == []:
                 count = count + 1
                 print(f'{count}.', *k, *v)
             if v != []:
                 count = count + 1
                 print(f'{count}.', *k, *v)

     if "mark" in comm:
        students_append = input('-Данные студента- ').split()
        for k, v in students_mark.items():
             if v == []:
                 v.append(*list(map(int, students_append)))
                 print('OK')
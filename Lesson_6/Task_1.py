user_path_input = input('Введите путь к файлу: ')
with open(user_path_input, "r", encoding="utf-8") as f:
    try:
        files = max([elem for elem in f.read().split()], key=len)
        if files:
            print(files, " ", len(files))
    except ValueError:
        print('Not Found')
        #C:\Users\1\Desktop\Leve_Up\Lesson_6\Test.txt
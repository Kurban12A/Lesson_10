
# C:\Users\Курбан\Desktop\Курс Level UP\Lesson_10_1\del_comment.txt
try:
    with open(input('Введите путь до файла: '), 'r+', encoding='utf-8') as file:
        for line in file:
            if not line.strip().startswith("#"):
                print(line)
except FileNotFoundError:
    print('Нет файла по этому пути')

# 1
# ✔ Напишите функцию, которая принимает на вход строку —
#   абсолютный путь до файла. Функция возвращает кортеж из трёх
#   элементов: путь, имя файла, расширение файла.


def parse_abs_path(text_path):
    *prefix, file = text.split('\\')
    path = '\\'.join(prefix)
    file_name, file_extension = file.split('.')
    return path, file_name, file_extension


text = 'C:\\Users\\Ainur\\AppData\\Local\\Programs\\Python\\Python39\\python.exe'
result = parse_abs_path(text)
print(f'{result = }')

# Задание №1
# ✔ Пользователь вводит строку из четырёх
#   или более целых чисел, разделённых символом “/”.
#   Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#   хранятся в кортеже как значения второго ключа.


a, b, c, *d = input('Enter line: ').split('/')
dict_input = {b: a, c: [b, d]}
print(f'{dict_input = }')

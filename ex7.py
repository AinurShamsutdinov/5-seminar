# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
#   начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
#   правило: «число является простым, если делится
#   нацело только на единицу и на себя».


def generator_simp(amount):
    number = 2
    divider = 2
    while amount > 0:
        if number <= divider:
            number += 1
            divider = 2
            amount -= 1
            yield number - 1
        elif (number % divider) == 0:
            number += 1
            divider = 2
        else:
            divider += 1


for item in generator_simp(1000):
    print(item)

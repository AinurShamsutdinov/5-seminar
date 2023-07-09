# Задание №5
# ✔ Напишите программу, которая выводит
#   на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
#   программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
#   должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


def int_generator(start, end):
    for item in range(start, end):
        if (item % 3) == 0 and (item % 5) != 0:
            yield 'Fizz'
        elif (item % 3) == 0 and (item % 5) != 0:
            yield 'Buzz'
        elif (item % 3) == 0 and (item % 5) == 0:
            yield 'FizzBuzz'
        else:
            yield item


for i in int_generator(1, 100):
    print(i)

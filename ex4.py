# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
#   числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


int_iterator = (item for item in range(0, 100) if (((item % 10) + (item - (item % 10)) / 10) != 8) and (item % 2) == 0)

print(int_iterator)
for i in int_iterator:
    print(i)


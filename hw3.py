# 3
# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonachi(number):
    first = 0
    second = 1
    fibo = 0
    count = 0
    while count < number:
        fibo = first + second
        first = second
        second = fibo
        count += 1
        yield fibo


for i in fibonachi(20):
    print(i)

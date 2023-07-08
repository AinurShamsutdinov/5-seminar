# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
#   Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
#   обращаясь к итератору, а не к словарю.


text = 'Самостоятельно сохраните в переменной строку текста.'
text_recollected: str = str()

dict_text = {i: ord(i) for i in text}
dict_comprehensions = [i for i in dict_text.values()]
for i in dict_comprehensions:
    text_recollected += chr(i)
print(f'{text_recollected = }')
print(f'{dict_text = }')

dict_iterator = iter(dict_text)
print(next(dict_iterator))
print(next(dict_iterator))
print(next(dict_iterator))
print(next(dict_iterator))
print(next(dict_iterator))




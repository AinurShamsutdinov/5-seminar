# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


text = 'Самостоятельно сохраните в переменной строку текста.'
text_recollected: str = str()

dict_text = {i: ord(i) for i in text}
dict_comprehensions = [i for i in dict_text.values()]
for i in dict_comprehensions:
    text_recollected += chr(i)

print(f'{dict_text = }')
print(f'{text_recollected = }')

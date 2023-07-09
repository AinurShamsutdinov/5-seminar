# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


lst_name = ['Cartman', 'Kyle', 'Stan', 'Kenny']
lst_compensation = [100, 200, 400, 300]
lst_interest = ['50.12%', '30.84%', '90.49%', '70.39%']


bonuses = {name: (compensation / 100 * float(interest.replace('%', ''))) for name, compensation, interest in zip(lst_name, lst_compensation, lst_interest)}
print(bonuses)

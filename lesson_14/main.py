# Первый задача.
# phrase = " ЛУЧШЕ ВСЕХ ХОТЬ УБЕЙТЕ, Я ТОП 1 НА ПЛАНЕТЕ)  ".title().strip()
# print(phrase)
# symbols = list("!@#$%^&*()_+*/:;1234567890|'\",.?")  # \" - экранирование, прикол
# phrase_clear = ""  # щяс будем мыть фразу
# for _ in phrase:  # итерироваться по фразе
#    if _ not in symbols:  # если это не спец. символ
#        phrase_clear += _

# phrase_list = phrase_clear.split(" ")
# print(phrase_list)

# d = {}
# for dom in phrase_list:
#    if dom not in d:  # если ключа нет
#        d[dom] = 1  # обозначение нового эдемента {"я": 1}
#    else:  # если ключ есть
#        d[dom] += 1  # плюс один элемент
# print(d)

# Второй задача.
# sloj = 0
# d = {"Молоко": 100,
#     "Доширак": 21,
#     "Чипсы": 0.5,
#     "Богдан": 999}

# for i in d.values():  # перебор по значениям
#    sloj += i
# print(sloj)


# Тритий (за дачей).
DIE_SIDES = 6
DIE_COUNT = 2
d = {}

for first in range(1, DIE_SIDES + 1):  # от 1 до 6 включительно
    for second in range(1, DIE_SIDES + 1):
        if first + second not in d:  # если суммы кубиков нет в словаре
            d[first + second] = [(first, second)]
        else:  # если такой ключ уже есть
            d[first + second].append((first, second))  # добавляем вариант
# вывод
for tadjikistan in d:
    print(f"{tadjikistan}: {d[tadjikistan]}")



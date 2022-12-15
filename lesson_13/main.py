# МНОЖЕСТВА
# s = set()  # пустое множество
# s1 = {1, 2, 3, 3}  # дубликаты исключаются
# print(s1)

# s2 = {"А", "Б", "В"}  # не упорядоченный тип данных
# print(s2)

# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}
# print(s1.union(s2))  # объединяем s1 с s2
# print(s1 | s2)  # оператор объединения

# print(s1.intersection(s2))  # пересечение
# print(s1 & s2)  # оператор персечения

# print(s1.difference(s2))  # разность
# print(s1 - s2)  # оператор разности

# print(s1.symmetric_difference(s2))  # симметрическая разность
# print(s1 ^ s2)  # оператор симметрической разности


# СЛОВАРИ
# d = {}  # пустой словарь
# d1 = {"Пи": 3.14,
#      "Преподаватель": "Антон",
#      "Список дел": ["Выжить", "Ловить балдёж"],
#      "Словарь": {"Вл1" : 1}}

# print(d1["Преподаватель"])
# print(d1["Список дел"][1])
# print(d1["Словарь"]["Вл1"])

# from random import randint

# lst = []

# for _ in range(5):
#    lst.append(randint(1, 5))
# print(lst)

# unique = set(lst)
# print(unique)

# print(f"{len(unique)} штук: {unique}")


# from random import randint

# lst1 = []
# lst2 = []

# SIZE = randint(100, 1000)
# R_START = 0
# R_END = 10_000  # _ -  декоративный разделитель, чтоб не запутаться в нулях

# for _ in range(SIZE):
#    lst1.append(randint(R_START, R_END))
#    lst2.append(randint(R_START, R_END))
# set1 = set(lst1)
# set2 = set(lst2)

# inter = set1.intersection(set2)  # пересечение
# print(f"Общих чисел: {len(inter)}")
# print(f"[Количество генераций]: {SIZE}")
# print(f"[Максимальное значение]: {max(inter)}")
# print(f"[Минимальное значение]: {min(inter)}")
# возможное решение, но колхозное
# inter1 = list(inter)
# inter1.sort()
# print(inter1)
# print(sorted(inter))  # sorted() - сортирует + преобразование в список

set1 = set()
insert = ""
while insert != "end":
    insert = input("Ввод: ")
    if insert.lstrip("-").isdigit():  # если это число
        # .lstrip() - убирает символ x слева
        if insert not in set1:  # если числа не было
            print("НЕТ")
            set1.add(insert)
        else:
            print("ДА")
    elif insert == "end":
        break  # выход из while
    else:
        print("Число хочу. и молочного коктейля бы щяс кст.")




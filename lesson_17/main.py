# Лямбда(lambda) функции
# plus_one2 = lambda a, b: a + b + 1
# print(plus_one2(5, 4)

# if-else в lambda
# result = lambda: True if answer == "Д" else False

# List comprehension (генератор списка)
# spisok = []
# for i in range(1, 6):  # от 1 до 5
#    spisok.append(i)
# print(spisok)

# spisok2 = [n for n in range(1, 6)]
# 1. List comprehension всегда пишется в []
# 2. for n in range(1, 6)  обычный цикл for ->
# сколько будет элементов в списке
# 3. все что слева от for -> элемент списка
# print(spisok2)

# первый за дачей
# c2f = lambda c:c * 9/5 + 32
# f2c = lambda f:(f - 32) * 5/9
# c2k = lambda c:c + 273.15
# k2c = lambda k:k - 273.15
# f2k = lambda f:c2k(f2c(f))
# print(f2k(203))

# второй за дачей
# from random import randint
# banana = lambda exit_trigger: True if exit_trigger == "да" else False
# while True:
#    arbuz = int(input("сколько раз бросаешь куб?🎲"))
#    dies = [randint(1,6) for n in range(arbuz)]
#    print(dies)
#    kivi = input("выходишь? да/нет").strip()
#    banana(kivi)
#    if banana(kivi):  # если захотел выйти
#        break

# третий за дачей
# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#         list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#         list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#         list("abcdefghijklmnopqrstuvwxyz"),
#         list("1234567890")
#        ]

# cot = [choice(choice(chars)) for n in range(6)]
# cotik = "".join(cot)
# dictionaryy = {"https://www.google.com":"12345"}
# ssylka_na_kavkaz = "https://www.google.com"
# if ssylka_na_kavkaz in dictionaryy:
#    print("ссылка уже есть в базе, вот её кот:")  # выводим код ссылкой
#    print(dictionaryy[ssylka_na_kavkaz])
# else:
#    print("ссылка добавлена, держи кота с:", cotik)
#    dictionaryy[ssylka_na_kavkaz] = cotik

# четвёртый за особняк

u = lambda a, b:a / b
print(u(6, 3))
u2 = lambda a, b:a % b
print(u2(6, 3))
u3 = lambda a, b:a // b
print(u3(6, 3))
u4 = lambda a, b:a ** b
print(u4(6, 3))
u5 = lambda a: -a if a < 0 else a  # если отрицательное, меняем знак
print(u5(-6))




# x = int(input("Введи число: "))
#
# if 5 < x < 10:  # двойное неравенство
#     print("Ура!")  # pass - затычка
#
#if x < 10 and x > 5:  # два условия обязательны
#    print("Ура!")
#
#if x < 10 or x > 5:  # одно из условий
#    print("Ура!")

# Списки
# name_1 = "Тоха"
# name_2= "Антон"
# name_3 = "Тоша"
# mega_shastoon = [name_1, name_2, name_3]  # список
# # операции со списками:
# mega_shastoon.append("Шастун")  # добавить элемент в список
# mega_shastoon.pop(1)  # удалить по индексу
# mega_shastoon.remove("Тоха")  # удалить по значению
#
# print(mega_shastoon)

# Индексация несколько раз
# man = [["Эд, Арс"], ["Футбол, телевизор"], "Вера"]
# print(man[0][0])  # выводим арса
#
# number = float(input("Введи число: "))
# if number < 0:  # если
#     print("Отрицательное")
# elif number > 0:  # иначе если (else + if)
#     print("Положительное")
# else:  #  иначе
#     print("Число, на которое нельзя делить")
#
# year = int(input("Введи год: "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("високосненько 😊")
# else:
#     print("не високосненько ☹")
#
# number_1 = int(input("Введи число: "))
# operation = input("Введи операцию (+, -, /, *, **, |):").strip()
# # .strip - метод строки, убирающий пробелы нач и кон
# number_2 = int(input("Введи второе число: "))
# lst = ["+", "-", "/", "*", "**", "|"] # список допустимых операций
# if operation in lst:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "**":
#         print(number_1 ** number_2)
#     elif operation == "|":
#         print(abs(number_1), abs(number_2))
# abs() - получить модуль числа
#
# number_1 = int(input("Первое число: "))
# number_2 = int(input("Второе число: "))
# number_3 = int(input("Третье число: "))
#
# lst = [number_1, number_2, number_3]
# print("Максимальное число:", max(lst))
# print("Минимальное число:", min(lst))
# # min() - поиск минимума; max() - поиск максимума

ticket = input("Введи номер билета: ")
if len(ticket) == 6 and ticket.isdigit():  # 6 цифр в билете и это числа (положительные)
    first_half = ticket[:3]  # три первых числа
    last_half = ticket[-3:]  # три последних числа
    first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    last_sum = int(last_half[-3]) + int(last_half[-2]) + int(last_half[-1])
    if first_sum == last_sum:
        print("счастливенько 😁")
    else:
        print("несчастливенько ☹")
else:
    print("У тебя шляпа👒")
#x = 7
#if x == 5: # false
#    print("я не сработаю ☹")
#elif x > 5:
#    print("x > 5 🤓")
#else: # если не сработает if или elif
#    print("я, вероятно сработаю 😊")
#
# word_1 = input("Введи слово (1/2): ")
# word_2 = input("Введи слово (2/2): ")
#
# word_1 = word_1.lower()
# word_2 = word_2.lower()
#
# if word_1.isalpha() and word_2.isalpha():
#
#     sorted_w1 = sorted(word_1)
#     sorted_w2 = sorted(word_2)
#
#     print(sorted_w1)
#     print(sorted_w2)
#
#     if sorted_w1 == sorted_w2:
#         print("Ура, у вас анаграмма 😄")
#     else:
#         print("Ну не получилось ☹")
# else:
#     print("Хочу только буквы 🔤")

q1 = input("Скока будит 2 + 2\n"
           "а) 4, б) 5\n"
           "--> ")
if q1 == "а":
    print("праильна😎")
else:
    print("одна ошибка и ты ошибся🐺")
    quit()
q2 = input("Арбуз - это(с ботанической точки зрения)...?\n"
           "а) корнеплод, б) овощ, в) то,отчего обоссышься, г) ягода\n"
           "--> ")
if q2 == "г":
    print("праильна😎")
else:
    print("одна ошибка и ты ошибся🐺")
    quit()
q3 = input("Что такое цугцванг?\n"
           "а) положение в шашках и шахматах, в котором любой ход игрока ведёт к ухудшению его позиции\n"
           "б) mochila\n"
           "в) поджанр фф, посвящённый егору\n"
           "г) когда физически цепь замкнута, но ток не проходит\n"
           "--> ")
if q3 == "а":
    print("ну как бы да, в общем-то правильно🙂")
elif q3 == "в":
    print("партия гордится тобой. Плюс второй порция миска рис.😋")
else:
    print("ну нет, правильный ответ был 'в'")
    quit()
print("Ты победил, респектуха!🆒")
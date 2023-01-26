# Функции
# def functia(x):  # объявление функции
#    return x + 1

# print(functia(5))  # вызов функции с аргументом

# f = lambda x2: x2 + 1  # объявление лямбда функции
# print(f(5))  # вызов лямбда функции

# фасоль
# beans = 20
# def vichitanie(b):
#     global beans
#     beans -= b
#
#
# while beans > 0:
#     while True:  # валидация
#         first = int(input("Первый игрок сколько фасолей берёшь?: "))
#         if first < 4 and first > 0:
#             break
#     vichitanie(first)
#     print(beans)
#     if beans <= 0:
#         print("========== ПОБЕДИЛ ВТОРОЙ ИГРОК ==========")
#         break
#     while True:  # валидация
#         second = int(input("Второй игрок сколько фасолей берёшь?: "))
#         if second < 4 and second > 0:
#             break
#     vichitanie(second)
#     print(beans)
#     if beans <= 0:
#         print("========== ПОБЕДИЛ ПЕРВЫЙ ИГРОК ==========")
#         break

# from random import randint
# import time
# print("время проверить твою ловкость.Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter")
#
# input("нажми Enter чтобы начать...")
# print("время пострелять...")
# time.sleep(randint(2,5))
# input("СТРЕЛЯЙ!!!")
# start = time.time()
# input("СТРЕЛЯЙ!!!")
# end = time.time()
# delta = end-start
# print(delta)
# if delta > 0.3:
#     print("ты черепаха! стреляй быстрее!!🐢")
# elif delta < 0.01:
#     print("ты слишком быстрый!")
# else:
#     print("ура победа!!😎🏆")

from random import randint

a = int(input("сколько костьей кидаешь?: "))
d = {}
for i in range(a, a * 6 + 1):
    d[i] = 0
for b in range(1_000_000):
    total = 0
    for _ in range(a):
        brosok = randint(1,6)

        total += brosok
    d[total] += 1
    print(d)







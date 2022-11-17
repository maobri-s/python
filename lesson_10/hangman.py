# lst = [0, 1, 2, 3, 4, 5]
#
# for mega_anton in lst:
#     print(mega_anton)
#
# for super_anton in range(11):  # от 0 до 10 включительно
#     print(super_anton)
#
# x1 = int(input("Число: "))
# x2 = int(input("Число: "))
#
#
# while x1 <= x2:
#     print(x1)
#     x1 += 1 #то же самое что и x = x1+1
#
# for igor in range(x1, x2 + 1):
#     print(igor)
#
# while True:
#     try:
#         level = int(input("Ярусов: "))
#     except ValueError:  # букву в число
#         print("Хочу чиселко😕")
#         continue  # перезапускать while
#     else:  # если ошибок неть
#         break  # выход из while true
#
#
# while True:
#     char = input("Символ: ").strip()
#     if len(char) == 1:
#         break
#
# for i in range(1, level + 1):  # 1-(level) (level раз)
#     # левая половина
#     print(" " * (level-i), end="")
#     print(char * i, end="||")
#
#     # правая половина
#     print(char * i)
import random
import hangman_arts as art

print(art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary).lower()
word_display = []

for _ in range(len(word_answer)):
    word_display.append("_")

print(word_display)
life = 6
counter = 0  # количество проявленных букв


while life > 0 and counter != len(word_answer):
    print(art.stages[life])
    letter_is_be = False  # наличие буквы в слове
    # пока проявленных != букв в ответе и жизней > 0
    letter = input("Буква: ").lower()
    for i in range(len(word_answer)):  # пробегаемся по ответу
        if letter == word_answer [i]:  #  если бука
            if word_display[i] != "_":  # если буква отгадана
                letter_is_be = True
            else:  # если буква не отгадана
                word_display[i] = letter  # переворачиваем букву
                counter += 1  # проявленная буква
                letter_is_be = True
    if letter_is_be == False:  # если мимо
        life -= 1
    print(word_display)

if counter == len(word_answer):
    print("Пабеда🏆")
else:
    print(art.stages[life])
    print("Не получилось🙁")
    print(word_answer)

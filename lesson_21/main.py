# try:
#      number = int(input("Введи число: "))
# except (ValueError, IndexError):
#      print("понел")
# except IndexError:
#     print("ы")
# else:  # если исключения не пойманы
#      print("понел2")
# finally:  # сработает в любом случае
#      print("я поработав")
#
# name = input("Введи имя друга(собаки): ").title()
# try:
#     if name == "Маша":
#         raise ValueError("э, ты чо, пес")
# except ValueError as pelmeni:
# print(pelmeni, "запрещаю.🚫")

# первый за дачей
# def masha(content):
#     s = 0
#     k = 0
#     for chiselko in content:
#         try:
#             s += int(chiselko)
#         except ValueError:
#             print("найдено не число:", chiselko)
#         else:
#             k += 1
#         if k == 0:
#             print("чисел не было найдено.")
#             return "[здесь ничего нет]"  # выход из функции
#     return round(s / k, 3)


# try:
#     g = open("masha.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет, пока!")
#     quit()
# content = g.read().split()  # по пробелам и переносу строки
# g.close()
# print(masha(content))

# второй за дачей
# try:
#     g = open("masha.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет, пока!")
#     quit()
# content = g.readlines()
# g.close()
# print(content)
#
# for i, student in enumerate(content):
#     content[i] = student.split()
#
# maxi = -1
# for student in content:
#     try:
#         if int((student[3])) > maxi:
#             maxi = int(student[3])
#     except ValueError:
#         print("неверно указаны баллы", student)
#     except IndexError:
#         print("баллы отсутствуют", student)
# if maxi == -1:
#     print("нет записей об участниках")
#     quit()
# print(maxi)

# третий за дачей
try:
    g = open("masha.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("файла нет, пока!")
    quit()

content = g.read()
word = input("Какое слово мы ищем: ")
print(content.count(word))

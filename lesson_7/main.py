# ZeroDivisionError
# x = 5/0

# TypeError
# x = "a" + 15

# IndexError
# x = [0, -15, "Антон"]
# x[3]

# SyntaxError
# x = "Привет, я Маша.

# NameError
# x = "Я строчка"
# print(x2)

# assert --> AssertionError
#def summa(numbers):
#    return sum(numbers)
#
#
#print(summa([1,2])) == 3
#assert summa([1,2]) == 4


# try - попытаться
# except - отлавливание исключений
# else - иначе, если ошибок не было (если всё хорошо)
# finally - в любом случае
# try:
#     number = int(input())
#     x = 5 / number
# except ZeroDivisionError:
#     print("слышь ты, низя на нуль делить😝")
# except ValueError:
#     print("хочу циферки")
# except Exception:  # любая ошибка будет обработана
#     print("блин,ну ты ошибся!😕")
# else:  # else - когда всё хорошо🥰
#     print("я поделил☺")
# finally:
#     print("меня написала маша")
#
#
# print("я закончил работать.")


# PASS
# try:
#     number = int(input())
#     x = 5 / number
# except Exception:
#     pass  # затычка, ничего не произойдёт
#
# if 5 == 5:
#     pass  #TODO: дописать код
#
# try:
#     x = input("Введи имя: ")
#     if x == "Маша":
#         raise Exception("Машу в обиду не дам")
#     # raise - вызвать исключение или ошибку
# except Exception as error_message:
#     # as - сохранить ошибку в error_message
#     print("Это слово запрещено!", error_message)


ints = []
try:
    f = open("fd.txt")
except FileNotFoundError:
    print("ну не получилось☹")
else:
    try:
        for line in f:
            ints.append(int(line))
    except ValueError:
        print("тут не число")
    else:  # ошибок неть
        print(ints)
    finally:  #ваще всегда
        f.close()
        print("я закрыл фаел😁")


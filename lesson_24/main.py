# ИНКАПСУЛЯЦИЯ
# def __sad():
#     print("кире все равно")
#
#
# class Nazvanie:
#     def __init__(self):
#         self.money = 1_000  # public
#         self.__zarplata = 3  # private
#
#     def bar(self):
#         if self.__zarplata > 4:  # используем private
#             return True
#         else:
#             self.__sad()  # вызов private метод
#             return False
#
#     def __sad(self):  # private метод
#         print("кире все равно")
#
#
# kira = Nazvanie()
# print(kira.money)  # public можно выводить
# kira.money += 100  # public можно менять

# print(kira.__zarplata)  # private нельзя выводить
# kira.__zarplata = 10  # public
# kira.__zarplata += 10  # private нельзя изменять
# print(kira.__zarplata)
# print(kira.bar())
#
# kira._Nazvanie__zarplata = 1_000_000  # меняем private
# print(kira.bar())
# задача1
# class Avtomobil:
#     def zapusk(self):
#         return "Автомобиль заведён"
#     def otkluchenie(self):
#         return "Автомобиль заглушён"
#     def g(self, year):
#         self.year = year
#     def y(self, god):
#         self.god = god
#     def c(self, color):
#         self.color = color
#     def t(self, type):
#         self.type = type
#
#
#
# kira = Avtomobil()
# kira.c("чёрный")
# print(kira.color)
# kira.t("бэчбэк")
# kira.y(1893)
# print(kira.zapusk())
# print(kira.otkluchenie())

# задача2
# import string
# class Alphabet:
#     def __init__(self, lang):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#     def  print(self):
#         print(self.__letters)
#     def letters_num(self):
#         print(len(self.__letters))
#
# alina = Alphabet("eng")
# alina.print()
# alina.letters_num()

# задача3
import datetime
class Clock:
    def __init__(self):
        self.__time = "08:07:03"
        self.__h, self.__m, self.__s = self.__time.split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
        # self.m = self.__time.split(":")[1]
        # self.s = self.__time.split(":")[2]
    def hours(self):
        self.__h += 1
    def minutes(self):
        self.__m += 1
    def seconds(self):
        self.__s += 1
    def test_h(self):
        if self.__h > 23:
            self.__h = 0
    def test_m(self):
        if self.__m > 59:
            self.__m = 0
            self.__h += 1
    def test_s(self):
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
    def vivod(self):
        print(f"{str(self.__h).rjust(2,'0')}:{str(self.__m).rjust(2,'0')}:{str(self.__s).rjust(2,'0')}")




time_0 = Clock()
time_0.minutes()
# time_0.test_m()
time_0.vivod()









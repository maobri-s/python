# Классы
# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # установка значений атрибутов
#         self.name = imya
#     def __str__(self):
#         return "всем кискам пис✌🏻"
#
#
# eugenii = Person("Юджин", 40)
# liza = Person(vozrast=0, imya="Кристина")
#
# print(kris.name)
# print(eugenii.age)
#
# print(kris)

# class HelloWorld:
#     def __getitem__(self, key):
#         print("hello world", key)
#
# hi = HelloWorld()
#
# # !!! обрати внимание, что здесь нет print(), просто обращение по ключу
# hi[1732594]
#
# hi['Movavi']

# первый задачей
# from random import randint
#
#
# class Person:
#     def __init__(self, imya, familia, vozrast):
#         self.name = imya
#         self.f = familia
#         self.age = vozrast
#         self.grades = [randint(2,5)  for n in range(randint(5, 10))]
#         self.sa = sum(self.grades) / len(self.grades)
#
#     def __str__(self):
#         return f"{self.name} {self.f} {self.age}"
#
#     def greet(self):
#         return f"Привет, я {self.name} {self.f}, мне {self.age}"
#
#
# kira = Person("Кира", "Медведева", 23)
# print(kira.greet())
# print("Имя:", kira.name)
# print("Фамилия:", kira.f)
# print("Возраст:", kira.age)
# print(kira)
# print(kira.grades)
# print(kira.sa)
# violetta = Person("Виолетта", "Малышенко", 22)
# liza = Person("Лиза", "Андрющенко", 24)
# kris = Person("Крис", "Захарова", 28)
# students = [kira, violetta, liza, kris]
#
# dnevnik = {}
# for item in students:
#     dnevnik[item.name] = item.sa
# print(dnevnik)
# print(dnevnik.items())
# sorted_dnevnik = dict(reversed(sorted(dnevnik.items(), key=lambda item: item[1])))
#
# schetchik = 0
# for item in sorted_dnevnik:
#     schetchik += 1
#     print(f"{schetchik}. {item} - {sorted_dnevnik[item]}")

class Rectangle:
    def __init__(self, d1, d2):
        self.dot1 = d1
        self.dot2 = d2
    def ploshad(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return a * b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dot1 = Point(1, 237)
dot2 = Point(2, 493)
pryamoug = Rectangle(dot1, dot2)

print(pryamoug.ploshad())

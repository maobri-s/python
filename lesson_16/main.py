  # Словари
#  d = {}  # пустой словарь
#  d = dict()  # пустой словарь

#  d = {"Ключ1": 1,
#      10: "два",
#      True: "Ложь",
#       True: "Богдан",
#       " ": 0,
#       "": 45,
#       (1, 2, 3): "У"}

  # ФУНКЦИИ
# def hello_world():  # объявление функции
#     print("hello world")

#hello_world()  # вызов функции
#hello_world()  # вызов функции

# def func(imya):
#    print(imya, "777")

# name = input("Какое погоняло: ")
# func(imya=name)  # вызов функции с аргументом

# def slojenie(chislo1, chislo2):
#    result = chislo1 + chislo2
#    return result  # вернуть что-то из функции

# print(slojenie(0, 0))  # вывод результата функции(то что вернёт return)
# x = slojenie(5,3)

# def more_5(number):
#    if number > 5:
#        return True

# if more_5(8):  # если выполнится
#    print("Балдёж 😎")

# первый за дачей

# def is_sorted(spisok):
#    s = sorted(spisok)
#     if spisok == s:
#         return True
#
# spisok = [1, 0, 5, 6, 78, 123]
# if is_sorted(spisok):
#     print("хэппи хэппи хэппи😁")
# else:
#     print("я хочу пельменей☹")

# второй за дачей

def find_longest(tadjiki:list):
    francuzi = []

    for rossiane in tadjiki:
        francuzi.append(len(rossiane))
    maxim = max(francuzi)
    portugalci = francuzi.index(maxim)  # нашли индекс максимума
    return tadjiki[portugalci], maxim


uzbeki = ["еееееее", "уууууу", "ааааа"]
print(find_longest(uzbeki))

  # третий за дачей

  # def max_min(spisok):
  #     # schweizari = min(spisok)
  #     # schotlandzi = max(spisok)
  #
  #     belorusi = sorted(spisok)
  #     italyanci = belorusi[0]   # минимум
  #     tayzi = belorusi[-1]   # максимум
  #     return italyanci, tayzi
  #
  # spisok = [37, 46, 20, 49034, 96]
  # print(max_min(spisok))

  # четвёртый за дачей

  def is_prime(celoe_chislo):
      for vietnamzi in range(2, celoe_chislo + 1):
          if vietnamzi == celoe_chislo:  # дошли до конца
              return True
          if celoe_chislo % vietnamzi == 0:  # мы нашли делитель🦦
              break


  if is_prime(71359):
      print("prostoe chislo🐸")
  else:
      print("natural chislo🏳‍🌈")

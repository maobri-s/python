y = input()
u = set(y)  # получаем уникальные символы
if len(u) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
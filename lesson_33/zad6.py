y = input().split(" ")
u = int(y[0])
n = int(y[1])
a = int(y[2])
s = 0
for i in range(1, a+1):  # считаем итоговую цену бананов
    s += i * u
if n - s >= 0:  # если денег хватает
    print(0)
else:
    print(s - n)




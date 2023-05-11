y = int(input())
u = 0
for i in range(y):
    a = input()
    if a.count("1") >= 2:
        u += 1
print(u)
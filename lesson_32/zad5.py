y = int(input())
u = 0
for i in range(y):
    n = input()
    if n == "X++" or  n == "++X":
        u += 1
    elif n == "X--" or n== "--X":
        u -= 1
print(u)
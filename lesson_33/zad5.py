y = input().split(" ")
u1 = int(y[0])
u2 = int(y[1])
n = 0
while u1 <= u2:
    u1 *= 3
    u2 *= 2
    n += 1
print(n)
y = int(input())

for i in range(y):
    u = input()
    if len(u) > 10:
        n = u[0] + str(len(u) - 2) + u[-1]
        print(n)
    else:
        print(u)
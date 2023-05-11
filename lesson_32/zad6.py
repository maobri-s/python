a1 = input().upper()
anser = 0
a2 = input().upper()
for i in range(len(a1)):
    if a1[i] != a2[i]:
        if a1[i] < a2[i]:
            anser -= 1
            break
        elif a2[i]<a1[i]:
            anser += 1
            break
print(anser)

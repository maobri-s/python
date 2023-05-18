input()
y = input()
perexod = 0
uborka = 0
while perexod != len(y) - 1:
    if y[perexod] == y[perexod+1]:
        y = y[:perexod] + y[perexod+1:]
        uborka += 1
    else:
        perexod += 1
print(uborka)

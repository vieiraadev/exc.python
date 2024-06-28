d1, m1, y1 = map(int, input("data1: ").split("/"))
d2, m2, y2 = map(int, input("data2: ").split("/"))
b1 = (y1 % 4 == 0 and y1 % 100 != 0) or y1 % 400
dy1 = 365 * y1 + y1 // 4 - y1 // 400
dm1 = 0
for m in range(m1, 13):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        dm1 += 31
    elif m == 2:
        dm1 += 28
        if b1: dm1 += 1
    else:
        dm1 += 30
days1 = dy1 - dm1 + d1
b2 = (y2 % 4 == 0 and y2 % 100 != 0) or y2 % 400
dy2 = 365 * y2 + y2 // 4 - y2 // 400
dm2 = 0
for m in range(m2, 13):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        dm2 += 31
    elif m == 2:
        dm2 += 28
        if b2: dm2 += 1
    else:
        dm2 += 30
days2 = dy2 - dm2 + d2
dif_days = abs(days1 - days2)
print(f"Diferença de dias: {dif_days}")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = sum(a)**2 #получаем диапазон, в котором точно будет нужное число
c = 0
y = []
for c in range(1,b+1):
    if (
        c % a[0] == 0
        and c % a[1] == 0
        and c % a[2] == 0
        and c % a[3] == 0
        and c % a[4] == 0
        and c % a[5] == 0
        and c % a[6] == 0
        and c % a[7] == 0
        and c % a[8] == 0
        and c % a[9] == 0
        ):
        y.append(c)
print(y)
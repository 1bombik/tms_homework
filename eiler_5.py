first = int(input("Введи число начала диапазона:"))
last = int(input("Введи число конца диапазона:"))
a = []
for e in range(first, last+1):
    a.append(e)
b = sum(a)**2 #диапазон, в котором будет нужное число
y = []
for c in range(1,b+1):
    for x in range(min(a), max(a)):
        if c % x == 0:
            y.append(c)
print(y)
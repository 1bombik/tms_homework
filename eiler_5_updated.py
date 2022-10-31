import numpy as n

first = int(input("Введи число начала диапазона:"))
last = int(input("Введи число конца диапазона:"))
a = n.array([1])
x = first
for x in range(first, last+1):
    a = n.append(a, x)
y = n.lcm.reduce(a)
print(y)
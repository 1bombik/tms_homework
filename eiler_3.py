a = 13195
x = 2 #наименьшее простое число
b = 0
y = []
for b in range(1,a+1):
    c = (x**(b-1))-1 #малая теорема ферма
    if c % b == 0 and a % b == 0:
        y.append(b)
print("Простые делители числа", a, "-", y)
print("Максимальный простой делить числа", a, "-", max(y))

a = 600851475143
x = 2 #наименьшее простое число
b = 0
y = []
for b in range(1,a+1):
    c = (x**(b-1))-1 #малая теорема ферма
    if c % b == 0 and a % b == 0:
        y.append(b)
print("Простые делители числа", a, "-", y)
print("Максимальный простой делить числа", a, "-", max(y))

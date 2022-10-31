number = int(input("Какое по счёту простое число тебе нужно? - "))
y = []
x = 2
for b in range(1,100000):
    c = (x**(b-1))-1
    if c % b == 0:
        y.append(b)
print(y[number-1])

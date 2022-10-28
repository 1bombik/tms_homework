a = float(input("Write your 1st number:"))
x = input("What do we do?: (+,-,/,*)")
b = float(input("Write your 2nd number:"))
if x == "+":
    print(a + b)
elif x == "-":
    print(a - b)
elif x == "/":
    print(a / b)
elif x == "*":
    print(a * b)
else:
    print("Something went wrong, try again please...")
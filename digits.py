import random as r

amount = int(input("How much numbers? - "))
digit = str(input("What digit to find? - "))
l_numbers = [] #list with random numbers
random_number = ""
for i in range(1, amount + 1):
    random_number = str(r.randint(1,100))
    l_numbers.append(random_number)
    i += 1
string = "".join(l_numbers)
times = string.count(digit)
print("The random numbers are - ", l_numbers, end="\n" +
"Your digit was found " + str(times) + " times")
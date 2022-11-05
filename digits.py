import random as r

a = int(input("Enter your first digit from 1 to 20 - "))
b = int(input("Enter your second digit from 1 to 20 - "))
compare = int(input("How many times to compare? - "))
c = r.randint(1,20)
d = r.randint(1,20)
i = 1
ab = 0 #if ab is greater than cd
cd = 0 #if cd is greater than ab
for i in range(1, compare+1):
    if a + b > c + d:
        ab += 1
        c = r.randint(1,20)
        d = r.randint(1,20)
    else:
        cd += 1
print(ab, cd)
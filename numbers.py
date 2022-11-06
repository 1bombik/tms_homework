string = input("Where something here - ")
list_1 = []
for i in string:
    if i.isdigit() == True:
        list_1.append(i)
print(list_1)
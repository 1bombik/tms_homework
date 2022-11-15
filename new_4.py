string = "An apple a day keeps the doctor away"
dict_1 = {letter: string.count(letter) for letter in string}
print(dict_1)
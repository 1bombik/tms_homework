text = input("Enter your text here - ")
all_vowel = ["а","у","о","и","э","ы","я","ю","е","ё"]
vowel = 0
consonants = 0
for i in text:
    if i in all_vowel:
        vowel += 1
    else:
        consonants +=1
print(vowel, consonants)
import re

a = "HjkLMfsdSD"
b = re.findall(r'[a-z]{2}', a)
c = re.findall(r'[A-Z]{2}', a)
print("Количество пар нижнего регистра - ", len(b), "-", b)
print("Количества пар верхнего регистра - ", len(c), "-", c)
import re

f = False
arr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
with open('111111.txt', 'rt') as a:                         # открытие файла
    inp = a.read()
if not inp:                                                            # если файл пустой
  print("\n файл test.txt пустой. замените его на другой или переименуйте существующий *.txt файл")
  exit(0)
for s in re.finditer(r'\b\d+\b', inp):                        # распознование числа
    s = s.group()                                                   # рабочий буфер
    if re.fullmatch(r'.*0{5}.*', s):                            # проверка на число остановки программы
        f = True
    if f:
        print(*map(lambda x: arr[x], s))
    elif re.fullmatch(r'.*[02468]', s):                      # проверка на четность 
        for i in range(1, len(s), 2):
            print(s[i], s[i - 1], sep='', end='')
        if len(s) % 2:
            print(s[-1], end='')
        print()

import re

n = int(input('введите n = '))
while n < 1:
    n = int(input('введите пожалуйста число больше 0\n'))
f = False
arr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
       '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
with open('111111.txt', 'rt') as a:            # открытие файла
    inp = a.read()
if not inp:                                                            # если файл пустой
    print("\n файл test.txt пустой. замените его на другой или переименуйте существующий *.txt файл")
    exit(0)
for s in re.finditer(r'\b\d+\b', inp):         # распознование числа по шаблону
    s = s.group()
    if re.fullmatch(rf'{"0" * n}', s):         # проверка на число остановки программы
        f = True
    if f:
        print(*map(lambda x: arr[x], s))
    elif re.fullmatch(r'.*[02468]', s):        # проверка на четность
        for i in range(1, len(s), 2):
            print(s[i], s[i - 1], sep='', end='')
        if len(s) % 2:
            print(s[-1], end='')
        print()

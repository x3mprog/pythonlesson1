# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

a = input('Введите число (a):\n')
b = input('Введите цифру (b) которую нужно найти и посчитать в числе a')
count = 0

for i in a:
    if i == b:
        count += 1
else:
    print(f'Цифра {b} встречается в {a} - {count} раз')
# Выполнить логические побитовые операции «И», «ИЛИ» и др.
# над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

# 5 в двоичной системе счисления 101
# 6 в двоичной системе счисления 110

# Получим 100 потому что данный бит присутствует в двух операндах
print(f'101 & 110 = {101 & 110}')

# Получим 111 потому что скопировали из операнда 101 в 110 отсутствующий бит,
# так как он в одном присутствует и этого достаточно
print(f'101 | 110 = {101 | 110}')

# Получим 11 потому что бит присутствует в одном из, но так как это исключающее или
# значит не должен бит быть в обоих сразу
print(f'101 ^ 110 = {101 ^ 110}')

# Получим при сдвиге вправо 1 так как линейке битов мы сдвигаемся вправо
print(f'101 >> 2 = {0b101 >> 2}')

# Получим при сдвиге влево 20 что в двоичной системе счесления означает 0b10100 а было 0b101 то есть мы
# сдвинули два бита влево тем самым получили такой результат
print(f'101 << 2 = {0b101 << 2}')


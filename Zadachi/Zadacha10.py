# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


n = int(input('Введите количество монеток: '))
count1 = 0
count2 = 0
print('Вводите 1 или 0: ')
for i in range(n):
    temp = int(input())
    if temp == 0:
        count1 += 1
    if temp == 1:
        count2 += 1
if count1 > count2:
    res = count2
else:
    res = count1
print(f'Результат: {res}')
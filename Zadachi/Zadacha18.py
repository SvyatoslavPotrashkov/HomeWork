# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

n = int(input('Укажите размер массива: '))
array = []
for i in range(1, n+1):
    array.append(i)
print(array)
x = int(input('Укажите число Х: '))
number = 0
for i in range(1, n+1):
    if (x-array[i-1]) < x-number and x-array[i-1] > 0:
        number = i
print(array[number-1])

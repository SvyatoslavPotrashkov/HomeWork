#     Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

n1 = int(input('Укажите размер массива: '))
array = []
for i in range(1, n1+1):
    array.append(i)
print(array)
n2 = int(input('Укажите число Х: '))
count = 0
for i in range(1, n1+1):
    if array[i-1] == n2:
        count+=1
print(count)

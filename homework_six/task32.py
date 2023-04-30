#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
array = [random.randint(0,15) for _ in range(15)]
print(array)
min = int(input('Введите минимум '))
max = int(input('Введите максимум '))
result = []
for i in range(len(array)):
    if array[i] < max and array[i] > min:
        result.append(i)
print(result)        



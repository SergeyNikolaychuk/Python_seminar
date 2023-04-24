# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
import random
money = int(input('Введите количество монет '))
array = [random.randint(0,1) for _ in range(money)]
print(array)
reshka = orel = 0 
for i in array:
    if i == 0:
        reshka += 1 
    else:
        orel += 1
if reshka < orel:
    print(reshka)  
else:
    print(orel)      
            

               




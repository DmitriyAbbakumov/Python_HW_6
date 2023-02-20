# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint
lst_min = int(input("Введите минимальные элемент: "))
lst_max = int(input("Введите максимальный элемент: ")) 
 
lst = [randint(-20, 20) for _ in range(1, 20)]
print(lst)
 
def int_ind(lst):
    lst_res = []
    for i in range(len(lst)):
        if lst[i] >= lst_min and lst[i] <= lst_max:
            lst_res.append(i)
    return lst_res
 
print(int_ind(lst))
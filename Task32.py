# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list1 = [randint(0, 10) for i in range(10)]
print(list1)
list2= [i for i in list1 if list1.count(i)==1]
print(list2)
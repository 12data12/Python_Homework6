# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_odd_index(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"The sum of the list elements having odd indexes is: {sum}")

lst = list(map(int, input("Enter your numbers separated by a space: ").split()))
sum_odd_index(lst)
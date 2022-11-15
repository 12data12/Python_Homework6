# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

def CreateListFromNegatToPositive(N):
    numbers = [i for i in range(-abs(N), abs(N) + 1)]
    return(numbers)   

n = int(input('Enter an integer: '))
numbers = CreateListFromNegatToPositive(n)
print(numbers)
index1 = int(input('Enter the first element index: '))
index2 = int(input('Enter the second element index: '))

print(f'First element is {numbers[index1 - 1]}')
print(f'Second element is {numbers[index2 - 1]}')
print(f'The product of the element is {numbers[index1 - 1] * numbers[index2 - 1]}')
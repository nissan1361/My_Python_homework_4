# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
l1 = []
l2 = []
for i in range(n):
    l1.append(int(input('Введите элемент первого множества: ')))
for j in range(m):
    l2.append(int(input('Введите элемент второго множества: ')))
l3 = []
for i in l1:
    if i in l2 and i not in l3:
            l3.append(i)
l3.sort()
print(l3)
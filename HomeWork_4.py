# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# n = int(input("введите размр первого множества: "))
# first_list = []
# for i in range(n):
#     number = int(input("Введите число: "))
#     first_list.append(number)
# print(first_list)
# print()
#
# n = int(input("введите размр второго множества: "))
# second_list = []
# for i in range(n):
#     number = int(input("Введите число: "))
#     second_list.append(number)
# print(second_list)
# print()
#
# first_set = set(first_list)
# print(first_set)
# second_set = set(second_list)
# print(second_set)
# print()
# result_set = first_set.intersection(second_set)
# print(sorted(result_set))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("введите количество кустов: "))
garden = []
for i in range(n):
    a = int(input("введите урожайность куста: "))
    garden.append(a)

b = int(input("введите возле какого куста стоит модуль сборки урожая: "))

if b == (n - 1):
    print(f'Максимальное число ягод, которое вы собирёте: {garden[n - 1] + garden[0] + garden[n - 2]}')
elif b == 0:
    print(f'Максимальное число ягод, которое вы собирёте: {garden[n - 1] + garden[b] + garden[b + 1]}')
else:
    print(f'Максимальное число ягод, которое вы собирёте: {garden[b] + garden[b - 1] + garden[b + 1]}')

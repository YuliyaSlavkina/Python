# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
#
# def make_journal(x):
#     journal = [int(input()) for i in range(x)]
#     return journal
#
#
# def swap_mark(lst):
#     maxx = max(lst)
#     minn = min(lst)
#     for i in range(len(lst)):
#         if lst[i] == maxx:
#             lst[i] = minn
#     return lst
#
#
# n = int(input("Введите количество оценок в журнале: "))
# print(swap_mark(make_journal(n)))
#
#
# Задача №31. Последовательностью Фибоначчи называется
# последовательность чисел a0 , a1 , ..., an, ..., где
# a0 = 0, a1=1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# x = int(input())
# print(fib(x))
#
# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
#
#
# def simple(number):
#     for i in range(2, number):
#         if number % 2 == 0:
#             return "no"
#         return "yes"
#
#
# n = int(input())
# print(simple(n))
#
#
# Задача №37. Дано натуральное число N и
# последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
#
#
# def foo(n):
#     elem = int(input('Введите число: '))
#     if n != 1:
#         foo(n - 1)
#     print(elem, end=' ')
#
#
# num = int(input('Введите размер списка: '))
# foo(num)
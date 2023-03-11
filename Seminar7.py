# a = [i if i % 2 == 0 else 0 for i in range(1, 9) ]


# lambda, filter, map, zip, enumerate, list comprehension
# list comprehension
# a = [i if i%2==0 else 0 for i in range(1,9) ]
# print(a)

# enumerate
# a = [0, 2, 0, 4, 0, 6, 0, 8]
# for a,r in enumerate(a):
#     print(indx,value)

# lambda
# def summa(a,b):
#     return a+b

# summa = lambda a,b:a+b
# print(summa(3,4))

# map
# a = [(12,2), (3,5), (45, 6)]
# a = list(map(lambda x: x[0]+x[1],a))
# print(a)

# filter
# a = [12, 3,45, 6]
# a = list(filter(lambda x: True if x*2>20 else False ,a))
# print(a)

# zip
# a = [1,2,3,4]
# b = "abcdef"
# d = dict(zip(a,b))
# print(d)


# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать): transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] или любой
# другой список transormed_values = list(map(transformation, values)) Единственный способ вашего взаимодействия с
# этим кодом - посредством задания функции transformation. Однако вы поняли, что для вашей текущей задачи вам не
# нужно никак преобразовывать список значений, а нужно получить его как есть. Напишите такое лямбда-выражение
# transformation, чтобы transformed_values получился копией values.

# transformation = lambda x: x
# values = [1, 23, 42, "asdfg", 78, 56, 32, 45]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")


# Задача №49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди
# списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы
# знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая
# орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S =
# pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще
# всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна Пример ввода и вывода данных
# представлены на следующем слайде

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit = list(map(lambda x: x[0]*x[1] if x[0] != x[1] else False, orbits))
# print(*orbits[find_farthest_orbit.index(max(find_farthest_orbit))])


# второе решение
# def find_farthest_orbit(list_of_orbits):
#     return max(list_of_orbits, key=lambda x: x[0] * x[1] if x[0] != x[1] else 0)
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(find_farthest_orbit(orbits))

# Задача. Отсортируйте список чисел по возрастанию средней цифры элементов списка
# nums = [197, 572, 234, 568, 654]
# sorted_nums = [234, 654, 568, 572, 197]

# nums = [197, 572, 234, 568, 654]
# sorted_nums = sorted(nums, key=lambda x: int(str(x)[1]))
# # int(str(x)[1])  перевели снвчала в строку число и указали что сортируем по первому индексу, в данном случае по 2му
# # числу
# print(sorted_nums)


# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент
# characteristic - это функция, которая

# values = [2, 10, 6, 11]
# a = lambda x: "same" if x % 2 != 1 else "different"
# res = list(map(a, values))
# print("different" if "different" in res else "same")

# второе решение

# def same_by(characteristic, objects):
#     return len(list(filter(characteristic, objects))) == 0
#
#
# # return all(map(characteristic, objects))
# #     тогда в условии нужно прописать x % 2 == 0
#
#
# values = [0, 2, 10, 6, 8, 12, 24, 1]
#
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")


# Задача 41. Напишите программу на Python для поиска пересечения двух
# заданных массивов с помощью Lambda, filter.
# a1 = [1, 2, 3, 5, 7, 8, 9, 10]
# a2 = [1, 2, 4, 8, 9]
#
# new_list = list(filter(lambda x: x in a1, a2))
# print(new_list)

# Задача. Имеется упорядоченный список: # Перебрать все элементы этого списка с помощью функций enumerate и элементы,
# стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# for indx, value in enumerate(a):
#     for indxIn, valueIn in enumerate(a):
#         if indxIn == indx:
#             a[indx][indxIn] = 0
# print(a)


# Задача 43. Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с
# помощью list_comprehension) Имеется список имен сотрудников из 10 элементов (вручную). Сопоставьте каждому имени
# сотрудника его id по порядку, и выведите получившийся список кортежей. Отсортировать список по возрастанию id.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda
# import random
#
# id = [random.randint(1, 100) for i in range(10)]
# names = ["Ivanov", "Petrov", "Sidorov", "Popov", "Sokolov", "Johansson", "Olsson", "Svensson", "Larsson", "Nilsson"]
#
# new_list = list(zip(id, names))
# print(new_list)
# new_list = sorted(new_list, key=lambda x: x[0])
# new_list = list(filter(lambda x: x[0] % 2, new_list))
# print(new_list)

# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d  Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
#
# line = input("Введите вашу строку: ").split()
# # разобьем split() разбивает строчку по указанному аргументу в скобках, по умолчанию пробел, поэтому список разобьется по
# # элементам до и после пробела
# result = {}
# # создаем словарь, ключами сделаем буквы а значением то какое кол-во раз встречаются буквы в строке
# for i in line:
#     if i in result:
#         print(f"{i}_{result[i]}", end=" ")
# # end=" " чтоб заменить перенос строки на пробел
#     else:
#         print(i, end=" ")
#     result[i] = result.get(i, 0) + 1
# print(result)

# Второе решение без .get
# line = input("Введите вашу строку: ").split()
# result = {}
# for i in line:
#     if i in result:
#         print(f"{i}_{result[i]}", end=" ")
#         result[i] += 1
#     else:
#         print(i, end=" ")
#         result[i] = 1
#
# print(result)

# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea " \
#        "shells on the sea shore I'm sure that the shells are sea shore shells"
# text_list = text.split()
# # разбили сразу нашу строку при помощи split на отдельные слова
# result = set()
# # создали множество, где не повторяются элементы
# for i in text_list:
#     result.add(i.lower())
# # при помощи .lower() все наши слова привели к общему виду - с маленькой буквы
# print(len(result))


# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам. Примечание: Программные коды на следующих слайдах

n = int(input())
max_num = n
while n != 0:
    # пользователь может вводить числа до тех пор пока не введёт ноль
    n = int(input())
    if n > max_num:
        max_num = n
print(f"Максимальное число:  {max_num}")

def get_op():
    op = int(input("1 - импорт. \n 2 - экспорт. \n 3 - удалить. \n 4 - изменить. \n  5 - выход. \n "))
    return op


def get_data():
    print('Введите новые данные: ')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    telephone = input('Телефон: ')
    data_str = name + ' ' + surname + ' ' + telephone + '\n'
    return data_str


def find_person():
    data_str = input('Введите параметр поиска: ')
    return data_str


def delete_data():
    data_str = input('Введите характеристику для удаления строки: ')
    return data_str


def choose_str():
    answer = int(input('Введите строку, хоторую хотите удалить: '))
    return answer




def get_op():
    op = int(input("1 - импорт. \n 2 - экспорт. \n 3 - выход. \n  "))
    return op

def get_data():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    telephone = input('Телефон: ')
    data_str = name + ' ' + surname + ' ' + telephone + '\n'
    return data_str

def find_person():
    data_str = input('Введите параметр поиска: ')
    return data_str
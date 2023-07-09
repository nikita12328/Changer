from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')



def print_data():
    print('1 Файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

    print('2 Файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))


def delite_data():
    print('Содержимое телефонной книги:\n'
          'NAME;SURNAME;PHONE;ADDRESS')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    for key, line in enumerate(lines):
        print(f'{key}: {line}')
    str_to_delete = int(input('Введите номер строки, которую нужно удалить: '))
    del lines[str_to_delete]
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print(f'Данные успешно удалены!')



def change_data():
    print('Содержимое телефонной книги:'
          'NAME;SURNAME;PHONE;ADDRESS')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    for key, line in enumerate(lines):
        print(f'{key}: {line}')
    str_to_change = int(input('Введите номер строки, в которой нужно изменить данные: '))
    temp_str = lines[str_to_change].split(';')
    print('Замените старые данные на новые..')
    temp_str[0], temp_str[1], temp_str[2], temp_str[3] = input_user_data()
    lines[str_to_change] = ';'.join(temp_str)

    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print(f'Данные успешно записаны!')

    

    
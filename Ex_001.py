from os.path import exists
from csv import DictReader, DictWriter

def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()

def get_info():
    info = []
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('invalid number')
            else:
                flag = True
        except ValueError:
            print('invalid number')
    info.append(phone_number)
    return info


def write_file(lst):
    with open('phone.csv', 'a', encoding='utf-8') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        f_n_writer.writerow(obj)
    with open('phone.csv', 'r+', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)

def update_info():
    if not exists('phone.csv'):
        print('Файл не создан')
        return

    phone_book = read_file('phone.csv')
    last_name = input('Введите фамилию человека, информацию о котором вы хотите изменить: ')

    updated = False
    for person in phone_book:
        if person['Фамилия'] == last_name:
            print('Текущая информация:')
            print(f'Фамилия: {person["Фамилия"]}, Имя: {person["Имя"]}, Номер: {person["Номер"]}')
            new_last_name = input('Введите новую фамилию (или оставьте пустым, чтобы не изменять): ')
            new_first_name = input('Введите новое имя (или оставьте пустым, чтобы не изменять): ')
            new_phone_number = input('Введите новый номер (или оставьте пустым, чтобы не изменять): ')

            if new_last_name:
                person['Фамилия'] = new_last_name
            if new_first_name:
                person['Имя'] = new_first_name
            if new_phone_number:
                person['Номер'] = new_phone_number

            updated = True
            break

    if updated:
        with open('phone.csv', 'w', encoding='utf-8') as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            for person in phone_book:
                f_n_writer.writerow(person)
        print('Информация обновлена')
    else:
        print('Человек с указанной фамилией не найден')

def search_by_last_name():
    if not exists('phone.csv'):
        print('Файл не создан')
        return

    last_name = input('Введите фамилию для поиска: ')
    phone_book = read_file('phone.csv')

    found = False
    for person in phone_book:
        if person['Фамилия'] == last_name:
            print(f'Фамилия: {person["Фамилия"]}, Имя: {person["Имя"]}, Номер: {person["Номер"]}')
            found = True

    if not found:
        print('Человек с указанной фамилией не найден')

def delete_info():
    if not exists('phone.csv'):
        print('Файл не создан')
        return

    phone_book = read_file('phone.csv')
    last_name = input('Введите фамилию человека, информацию о котором вы хотите удалить: ')

    deleted = False
    new_phone_book = []
    for person in phone_book:
        if person['Фамилия'] != last_name:
            new_phone_book.append(person)
        else:
            deleted = True

    if deleted:
        with open('phone.csv', 'w', encoding='utf-8') as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            for person in new_phone_book:
                f_n_writer.writerow(person)
        print('Информация удалена')
    else:
        print('Человек с указанной фамилией не найден')


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'u':  
            update_info()
        elif command == 'd':  
            delete_info()
        elif command == 's':
            search_by_last_name()
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            phone_book = read_file('phone.csv')
            for person in phone_book:
                print(f'Фамилия: {person["Фамилия"]}, Имя: {person["Имя"]}, Номер: {person["Номер"]}')
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()

main()
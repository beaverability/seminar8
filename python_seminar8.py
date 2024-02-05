# Создать телефонный справочник с возможностью
# импорта и экспорта данных в формате .txt. Фамилия,
# имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.
# 5. Дополнить справочник возможностью копирования данных из одного файла
# в другой. Пользователь вводит номер строки, которую необходимо
# перенести из одного файла в другой.

import csv
from typing import List


def copy_to_file(file, data, export_ind):
    list_contacts = []
    counter = 0
    if len(data) > 0:
        for i in export_ind:
            line = data[i - 1].split(', ')
            list_contacts.append({})
            list_contacts[counter]['last_name'] = line[1]
            list_contacts[counter]['first_name'] = line[0]
            list_contacts[counter]['patronymic'] = line[2]
            list_contacts[counter]['phone_number'] = line[3]
            counter += 1

        try:
            with open(file, 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = list_contacts[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_contacts)
            print('File created')
        except Exception as exc:
            print('Error! File not created:', exc)

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('There is no file. Create the file first\n')
        return []


def show_data(data: list):
    for line in data:
        print(line)


def save_data(file):
    first_name = input('Enter the name: ')
    last_name = input('Enter the last name: ')
    patronymic = input('Enter the patronymic: ')
    phone_number = input('Enter the phone number: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')


def search_data(contacts: List[str]):
    search_str = input('Enter the last name for search: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded


def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - Exit')
        print('1 - Write in file')
        print('2 - Show data in file')
        print('3 - Search data in file')
        print('4 - Copy the string in other file')
        answer = input('Choose the action: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            print("Enter file name", end=' ')
            csv_file_name = input().strip() + '.csv'
            data = read_file(file_name)
            show_data(data)
            print('Enter the string: ')
            export_num = list(map(int, input().split(',')))
            if max(export_num) > len(data):
                print('Uncorrected value')
            else:
                copy_to_file(csv_file_name, data, export_num)


if __name__ == '__main__':
    main()

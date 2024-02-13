import csv
from typing import List, Dict, Optional

PhoneBookEntry = Dict[str, str]
PhoneBookData = List[PhoneBookEntry]


def display_menu():
    print("\nМеню телефонного справочника:")
    print("1. Отобразить записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Найти записи")
    print("5. Выйти")


def get_entry_from_user() -> PhoneBookEntry:
    entry = {
        'Last name': input("Введите фамилию: "),
        'First name': input("Введите имя: "),
        'Middle name': input("Введите отчество: "),
        'Organization': input("Введите организацию: "),
        'Work phone': input("Введите рабочий телефон: "),
        'Personal phone': input("Введите личный телефон: ")
    }
    return entry


class PhoneBook:
    """
    Класс для работы с телефонным справочником
    """

    def __init__(self, filename: str):
        """
        Инициализация телефонного справочника.

        :param filename: Имя файла для хранения данных
        """
        self.filename = filename
        self.entries = self.load_entries()

    def load_entries(self) -> PhoneBookData:
        """
        Загрузка данных из файла.

        :return: Список записей из справочника
        """
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def save_entries(self):
        """
        Сохранение данных в файл
        """
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Last name', 'First name', 'Middle name', 'Organization', 'Work phone', 'Personal phone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.entries)

    def add_entry(self, entry: PhoneBookEntry):
        """
        Добавление новой записи в справочник.
        :param entry: Словарь с данными новой записи
        """
        self.entries.append(entry)
        self.save_entries()

    def edit_entry(self, index: int, change_item: str):
        """
        Редактирование записи в справочнике.

        :param index: Индекс записи для редактирования.
        :param change_item: Словарь с обновленными данными записи.
        """
        if 0 <= index < len(self.entries):
            if change_item.lower() == 'все':
                entry = get_entry_from_user()
                self.entries[index - 1] = entry
            elif change_item.lower() == 'фамилия':
                self.entries[index - 1]['Last name'] = input("Введите фамилию: ")
            elif change_item.lower() == 'имя':
                self.entries[index - 1]['First name'] = input("Введите имя: ")
            elif change_item.lower() == 'отчество':
                self.entries[index - 1]['Middle name'] = input("Введите отчество: ")
            elif change_item.lower() == 'организация':
                self.entries[index - 1]['Organization'] = input("Введите организацию: ")
            elif change_item.lower() == 'рабочий телефон':
                while True:
                    new_number = input("Введите рабочий телефон: ")
                    if new_number.isdigit():
                        self.entries[index - 1]['Work phone'] = new_number
                        print("Запись успешно изменена")
                        break
                    print("Неверное значение. Попробуйте еще раз.")
            elif change_item.lower() == 'личный телефон':
                while True:
                    new_number = input("Введите личный телефон: ")
                    if new_number.isdigit():
                        self.entries[index - 1]['Personal phone'] = new_number
                        print("Запись успешно изменена")
                        break
                    print("Неверное значение. Попробуйте еще раз.")
            else:
                print("Неверное поле. Попробуйте еще раз.")
            self.save_entries()
        else:
            print("Неверный индекс. Попробуйте еще раз.")

    def search_entries(self, search_term: str) -> Optional[PhoneBookData]:
        """
        Поиск записей по одной или нескольким характеристикам.

        :param search_term: Поисковый запрос
        :return: Список найденных записей или None, если ничего не найдено
        """
        results = [entry for entry in self.entries if any(search_term in value.lower() for value in entry.values())]

        return results if results else None

    def display_entries(self):
        """
        Вывод всех записей из справочника на экран
        """
        count = 0
        for entry in self.entries:
            count += 1
            print(
                f'{count}. Фамилия: {entry["Last name"]}, Имя: {entry["First name"]}, '
                f'Отчество: {entry["Middle name"]}, Организация: {entry["Organization"]}, '
                f'Рабочий телефон: {entry["Work phone"]}, Личный телефон: {entry["Personal phone"]}')

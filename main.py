from utils import PhoneBook, display_menu, get_entry_from_user


def main():
    phone_book = PhoneBook('phonebook.csv')

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            phone_book.display_entries()

        elif choice == '2':
            entry = get_entry_from_user()
            phone_book.add_entry(entry)

        elif choice == '3':
            index = int(input("Введите индекс записи для редактирования: "))
            change_item = input(
                "Какое поле вы хотите изменить(Фамилия/Имя/Отчество/Организация/Рабочий телефон/Личный телефон)? "
                "Если хотите поменять все поля, введите 'Всё': ")
            phone_book.edit_entry(index, change_item)

        elif choice == '4':
            search_term = input("Введите поисковый запрос: ")
            results = phone_book.search_entries(search_term)
            if results:
                for result in results:
                    print(
                        f'Фамилия: {result["Last name"]}, Имя: {result["First name"]}, '
                        f'Отчество: {result["Middle name"]}, Организация: {result["Organization"]}, '
                        f'Рабочий телефон: {result["Work phone"]}, Личный телефон: {result["Personal phone"]}')
            else:
                print("Записи не найдены.")

        elif choice == '5':
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()

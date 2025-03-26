import json
from csv import DictReader

from files import USER_JSON_FILE_PATH
from files import BOOKS_CSV_FILE_PATH


def get_user_info(file) -> list[dict]:
    """
    Чтение json файла пользователей.
    Функция возвращает список словарей пользователей.
    """

    with open(file, newline='') as f:
        users = json.load(f)
        users_list: list[dict] = []

        for user in users:
            # сбор информации о конкретном пользователе
            user_dict: dict = {
                'name': user.get('name'),
                'gender': user.get('gender'),
                'address': user.get('address'),
                'age': user.get('age'),
                'books': [],
            }
            # добавление пользователя в список пользователей
            users_list.append(user_dict)

    return users_list


def get_book_info(file) -> list[dict]:
    """
    Чтение csv файла книг.
    Функция возвращает список словарей книг.
    """

    with open(file, 'r') as f:
        books = DictReader(f)
        book_list: list[dict] = []

        for book in books:
            # получение информации о каждой отдельной книге
            book_dict: dict = {
                'title': book.get('Title'),
                'author': book.get('Author'),
                'pages': book.get('Pages'),
                'genre': book.get('Genre'),
            }
            # добавление книги в список книг
            book_list.append(book_dict)

    return book_list


def get_result_data(user_list: list, book_list: list) -> list:
    """
    Раздача книг пользователям.
    Функция принимат список пользователей и список книг,
    возвращает список для финальной загрузки данных в файл 'result.json'
    """

    while book_list:

        for i in range(len(user_list)):

            try:
                user_list[i]['books'].append(book_list[i])

            except IndexError:
                return user_list

        book_list = book_list[len(user_list):]


def create_result_json(a) -> None:
    """
    Загрузка итогового списка в файл json.
    """

    with open('result.json', 'w') as f:
        data = json.dumps(a, indent=4)
        f.write(data)


if __name__ == '__main__':
    create_result_json(
        get_result_data(
            user_list=get_user_info(USER_JSON_FILE_PATH),
            book_list=get_book_info(BOOKS_CSV_FILE_PATH),
        )
    )

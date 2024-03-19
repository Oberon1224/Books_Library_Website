#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, current_app
from .function import check_book_on_user

change_state = Blueprint('change_state', __name__, template_folder = 'templates')

@change_state.route('/<login>/change_on_favorite/<id_book>', methods = ['POST', 'GET'])
def change_on_favorite(login: str, id_book: int) -> str:
    """Запрос для добавление/изменения книги в избранное

    Args:
        login (str): Имя пользователя
        id_book (int): id книги

    Результаты выполнения условий:
        :if check_book_on_user: выполняется запрос update для таблицы list_states \n
        :else: выполняется запрос insert для таблицы list_states

    Returns:
        :str: Возвращает пустую строку
    """

    if check_book_on_user(current_app.config['LIST_STATES'].select_user_books(login), id_book):
        print(f'Книга с ID = {id_book} имеется у пользователя с логином {login}')
        current_app.config['LIST_STATES'].update_state(2, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    else:
        print(f'Книга  с ID = {id_book} отсутствует у пользователя с логином {login}')
        current_app.config['LIST_STATES'].insert_get_data(1, 2, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    return 'None'

@change_state.route('/<login>/change_in_read/<id_book>', methods = ['POST', 'GET'])
def change_in_read(login: str, id_book: int) -> str:
    """Запрос для добавление/изменения книги на чтение

    Args:
        login (str): Имя пользователя
        id_book (int): id книги

    Результаты выполнения условий:
        :if check_book_on_user: выполняется запрос update для таблицы list_states \n
        :else: выполняется запрос insert для таблицы list_states

    Returns:
        :str: Возвращает пустую строку
    """

    if check_book_on_user(current_app.config['LIST_STATES'].select_user_books(login), id_book):
        print(f'Книга с ID = {id_book} имеется у пользователя с логином {login}')
        current_app.config['LIST_STATES'].update_state(1, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    else:
        print(f'Книга  с ID = {id_book} отсутствует у пользователя с логином {login}')
        current_app.config['LIST_STATES'].insert_get_data(1, 1, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    return 'None'

@change_state.route('/<login>/change_end_read/<id_book>', methods = ['POST', 'GET'])
def change_end_read(login: str, id_book: int) -> str:
    """Запрос для добавление/изменения книги в прочитанное/на прочитанное

    Args:
        login (str): Имя пользователя
        id_book (int): id книги

    Результаты выполнения условий:
        :if check_book_on_user: выполняется запрос update для таблицы list_states \n
        :else: выполняется запрос insert для таблицы list_states

    Returns:
        :str: Возвращает пустую строку
    """
    
    if check_book_on_user(current_app.config['LIST_STATES'].select_user_books(login), id_book):
        print(f'Книга с ID = {id_book} имеется у пользователя с логином {login}')
        current_app.config['LIST_STATES'].update_state(3, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    else:
        print(f'Книга  с ID = {id_book} отсутствует у пользователя с логином {login}')
        current_app.config['LIST_STATES'].insert_get_data(1, 3, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
    return 'None'
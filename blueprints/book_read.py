from flask import Blueprint, render_template, current_app, request
from .function import check_book_on_user

book_read = Blueprint('book_read', __name__, template_folder='templates')

@book_read.route('/<login>/open/<id_book>', methods = ['POST', 'GET'])
def open_book(login: str, id_book: int) -> render_template:
    """Переход на страницу открытия книги

    Args:
        login (string): Имя пользователя
        id_book (int): id книги

    Результаты выполнения условий:
        :if check_book_on_user: выполняется запрос update для таблицы list_states \n
        :else: выполняется запрос insert для таблицы list_states

    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :open_book.html: Возвращает страницу чтения книги \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n

    """ 
    if current_app.config['USER_LOGIN']:
        if check_book_on_user(current_app.config['LIST_STATES'].select_user_books(login), id_book):
            print(f'Книга с ID = {id_book} имеется у пользователя с логином {login}')
            current_app.config['LIST_STATES'].update_state(1, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
        else:
            print(f'Книга  с ID = {id_book} отсутствует у пользователя с логином {login}')
            current_app.config['LIST_STATES'].insert_get_data(1, 1, id_book, current_app.config['USER'].select_id_on_login(login)[0][0])
        return render_template('open_book.html', login=login, id_book = id_book, style = current_app.config['STYLE'],
                               book = current_app.config['BOOK'], list_states = current_app.config['LIST_STATES'],
                               notes = current_app.config['NOTE'], tags = current_app.config['TAG'], 
                               language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'], 
                               id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@book_read.route('/change_page_marker', methods = ['POST', 'GET'])
def change_page_marker() -> str:
    """Запрос изменения страницы закладки

    Переменные:
        :new_page (str): Новая страница закладки \n
        :id_book (int): id книги \n
        :id_user (int): id пользователя

    Результаты выполнения условий:
        :if id_book and id_user and new_page: выполняется запрос update для таблицы list_states \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """ 
    new_page = request.form.get('new_page')
    id_book = request.form.get('id_book')
    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0]
    if id_book and id_user and new_page:
        current_app.config['LIST_STATES'].update_state_page(new_page, id_book, id_user)
        print(f'Страница-закладка книги с id = {id_book} для пользователя с id = {id_user} изменена на {new_page}')
    else:
        print('Новая страница, id книги или id пользователя со значением null!')
    return 'None'

@book_read.route('/add_note', methods = ['POST', 'GET'])
def add_note() -> str:
    """Запрос добавления заметки

    Переменные:
        :text_note (str): Новая заметка \n
        :id_book (int): id книги \n
        :id_user (int): id пользователя

    Результаты выполнения условий:
        :if id_last_note and id_book and id_user: добавляется новая заметка для книги \n
        :else: ничего не выполняется, одна из переменных со значением null

    Returns:
        :str: Возвращает пустую строку
    """ 
    text_note = request.form.get('text_note')
    id_book = request.form.get('id_book')
    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0]
    if text_note:
        id_last_note = current_app.config['NOTE'].get_last_row()
        current_app.config['NOTE'].insert_get_data(text_note)
        if id_last_note and id_book and id_user:
            current_app.config['LIST_NOTES'].insert_get_data(id_last_note, id_book, id_user)
            print(f'Заметка с id = {id_last_note} для книги (id = {id_book} для пользователя (id = {id_user})) добавлена!')
        else:
            print('ID книги, заметки или пользователя со значением null!')
    else:
        print('Текст заметки со значением null!')
    return 'None'
#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, render_template, current_app, request

change_book_information = Blueprint('change_book_information', __name__, template_folder = 'templates')

@change_book_information.route('/change_title', methods = ['POST', 'GET'])
def change_title() -> str:
    """Запрос на изменение названия книги

    Переменные:
        :title (str): Новое название книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if title and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """    
    title = request.form.get('title')
    id_book = int(request.form.get('id_book'))
    if title and id_book:
        current_app.config['BOOK'].update_title(title, id_book)
        print(f'Название книги с id = {id_book} изменено на "{title}" ')
    else:
        print('Название или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_page', methods = ['POST', 'GET'])
def change_page() -> str:
    """Запрос изменения количества страниц книги

    Переменные:
        :page (str): Новое количество страниц книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if page and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """    
    page = request.form.get('page')
    id_book = int(request.form.get('id_book'))
    if page and id_book:
        current_app.config['BOOK'].update_page(page, id_book)
        print(f'Количество страниц книги с id = {id_book} изменено на "{page}" страниц ')
    else:
        print('Количество страниц или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_path_book', methods = ['POST', 'GET'])
def change_path_book() -> str:
    """Запрос изменения пути к файлу книги

    Переменные:
        :path_book (str): Новый путь к файлу книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if path_book and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """    
    path_book = request.form.get('path_book')
    id_book = int(request.form.get('id_book'))
    if path_book and id_book:
        current_app.config['BOOK'].update_path_book(path_book, id_book)
        print(f'Путь к файлу книги с id = {id_book} изменен на "{path_book}" ')
    else:
        print('Путь к файлу книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_path_image', methods = ['POST', 'GET'])
def change_path_image() -> str:
    """Запрос изменения пути к изображению книги

    Переменные:
        :path_book (str): Новый путь к изображению книги \n
        :id_book (int): id книги

    Conditions:
        :if path_image and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """   
    path_image = request.form.get('path_image')
    id_book = int(request.form.get('id_book'))
    if path_image and id_book:
        current_app.config['BOOK'].update_path_image(path_image, id_book)
        print(f'Путь к изображению книги с id = {id_book} изменен на "{path_image}" ')
    else:
        print('Путь к изображению книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_category', methods = ['POST', 'GET'])
def change_category() -> str:
    """Запрос изменения категории книги

    Переменные:
        :category (str): Новая категория книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if category and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """   
    category = request.form.get('category')
    id_book = int(request.form.get('id_book'))
    if category and id_book:
        current_app.config['BOOK'].update_id_category(category, id_book)
        print(f'Категория книги с id = {id_book} изменена на "{category}" ')
    else:
        print('Категория книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_language', methods = ['POST', 'GET'])
def change_language() -> str:
    """Запрос изменения языка книги

    Переменные:
        :language (str): Новый язык книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if language and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """   
    language = request.form.get('language')
    id_book = int(request.form.get('id_book'))
    if language and id_book:
        current_app.config['BOOK'].update_id_language(language, id_book)
        print(f'Язык книги с id = {id_book} изменен на "{language}" язык')
    else:
        print('Язык книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_year', methods = ['POST', 'GET'])
def change_year() -> str:
    """Запрос изменения года издания книги

    Переменные:
        :year (str): Новый год издания книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if language and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """ 
    year = request.form.get('year')
    id_book = int(request.form.get('id_book'))
    if year and id_book:
        current_app.config['BOOK'].update_id_year(year, id_book)
        print(f'Год издания книги с id = {id_book} изменен на "{year}" год')
    else:
        print('Год издания книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/change_description', methods = ['POST', 'GET'])
def change_description() -> str:
    """Запрос изменения описания книги

    Переменные:
        :description (str): Новое описание книги \n
        :id_book (int): id книги

    Результаты выполнения условий:
        :if language and id_book: выполняется запрос update для выбранной книги \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """ 
    description = request.form.get('description')
    id_book = int(request.form.get('id_book'))
    if description and id_book:
        current_app.config['ABOUT'].update_information(description, id_book)
        print(f'Описание книги с id = {id_book} изменено на "{description}"')
    else:
        print('Описание книги или id книги со значением null!')
    return 'None'

@change_book_information.route('/<login>/change_book/<id_book>', methods = ['POST', 'GET'])
def change_book(login: str, id_book: int) -> render_template:
    """Переход на страницу изменения книги

    Args:
        login (string): Имя пользователя \n
        id_book (int): id книги

    Результаты выполнения условий:
        :if current_app.config: Переход на страницу change_book.html\n
        :else: Переход на страницу index.html

    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :change_book.html: Возвращает страницу изменения книги \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n

    """ 
    if current_app.config['USER_LOGIN']:
        return render_template('change_book.html', login=login, id_book = id_book, style = current_app.config['STYLE'],
                               tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                               year = current_app.config['YEAR'], category = current_app.config['CATEGORY'], 
                               book = current_app.config['BOOK'], author = current_app.config['AUTHOR'],
                               about = current_app.config['ABOUT'])
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

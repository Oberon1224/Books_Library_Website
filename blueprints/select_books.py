#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, render_template, current_app

select_books = Blueprint('select_books', __name__, template_folder = 'templates')

@select_books.route('/<login>/books/page/<int:page>', methods = ['POST', 'GET'])
def books(login: str, page: int) -> render_template:
    """Эта функция возвращает страницы с книгами

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewBooks): Модель представления базы данных view_books \n
        :page (int): Страница на которой находится пользователь (по умолчанию 1) \n
        :login (str): Логин пользователя \n
        :style (str): Стиль приложения \n
        :tags (Tag): Модель таблицы базы данных tag \n
        :authors (str): Модель таблицы базы данных authors \n
        :language (Language): Модель таблицы базы данных language \n
        :year (Year): Модель таблицы базы данных year \n  
        :category (str): Категория книг, необходимая для формирования перехода между страницами \n
        :state (State): Модель таблицы базы данных state \n
        :id_user (int): id пользователя
        
    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :books.html: Возвращает страницу с книгами если сессия работы с библиотекой  не завершена \n
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранной категорий \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """
    if(current_app.config['USER_LOGIN'] != None):
        if current_app.config['VIEW_BOOKS'].select_all() != None:
            return render_template('books.html',books = current_app.config['VIEW_BOOKS'].select_all(), 
                                page = page, login = login, style = current_app.config['STYLE'],
                                tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                category = 'books', state = current_app.config['STATE'],
                                id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])   
        else:
             print('В категории "Книги" отсутствуют книжные издания!')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR']) 
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@select_books.route('/<login>/article/page/<int:page>', methods = ['POST', 'GET'])
def article(login: str, page: int) -> render_template:
    """Эта функция возвращает страницу со статьями
    
    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewArticles): Модель представления базы данных view_articles \n
        :page (int): Страница на которой находится пользователь (по умолчанию 1) \n
        :login (str): Логин пользователя \n
        :style (str): Стиль приложения \n
        :tags (Tag): Модель таблицы базы данных tag \n
        :authors (str): Модель таблицы базы данных authors \n
        :language (Language): Модель таблицы базы данных language \n
        :year (Year): Модель таблицы базы данных year \n  
        :category (str): Категория книг, необходимая для формирования перехода между страницами \n
        :state (State): Модель таблицы базы данных state \n
        :id_user (int): id пользователя
        
    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :books.html: Возвращает страницу с книгами если сессия работы с библиотекой  не завершена \n
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранной категорий \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """
    if(current_app.config['USER_LOGIN']):
        if current_app.config['VIEW_ARTICLES'].select_all() != None:
            return render_template('books.html',books = current_app.config['VIEW_ARTICLES'].select_all(), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'article', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0]) 
        else:
            print('В категории "Книги" отсутствуют книжные издания!')
            return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                year = current_app.config['YEAR'])   
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@select_books.route('/<login>/joornal/page/<int:page>', methods = ['POST', 'GET'])
def joornal(login: str, page: int) -> render_template:
    """Эта функция возвращает страницы журналов

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewJoornals): Модель представления базы данных view_joornals \n
        :page (int): Страница на которой находится пользователь (по умолчанию 1) \n
        :login (str): Логин пользователя \n
        :style (str): Стиль приложения \n
        :tags (Tag): Модель таблицы базы данных tag \n
        :authors (str): Модель таблицы базы данных authors \n
        :language (Language): Модель таблицы базы данных language \n
        :year (Year): Модель таблицы базы данных year \n  
        :category (str): Категория книг, необходимая для формирования перехода между страницами \n
        :state (State): Модель таблицы базы данных state \n
        :id_user (int): id пользователя
        
    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :books.html: Возвращает страницу с книгами если сессия работы с библиотекой  не завершена \n
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранной категорий \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """
    if current_app.config['USER_LOGIN']:
        if current_app.config['VIEW_JOORNALS'].select_all() != None:
            return render_template('books.html',books = current_app.config['VIEW_JOORNALS'].select_all(), 
                                page = page, login = login, style = current_app.config['STYLE'],
                                tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                category = 'joornal', state = current_app.config['STATE'],
                                id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])   
        else:
            print('В категории "Книги" отсутствуют книжные издания!')
            return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                year = current_app.config['YEAR'])   
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  
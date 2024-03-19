#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, render_template, current_app, request

search_filter = Blueprint('search_filter', __name__, template_folder = 'templates')

@search_filter.route('/<login>/search/page/<int:page>', methods = ['POST', 'GET'])
def search(login: str, page: int) -> render_template:
    """Эта функция возвращает все найденные книжные издания

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewSearch): Модель представления базы данных search \n
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
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранным статусом \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """

    if current_app.config['USER_LOGIN']:
        if current_app.config['SEARCH_TITLE'] == None: 
            current_app.config['SEARCH_TITLE'] = request.form.get('search_input_field')
        if current_app.config['VIEW_SEARCH'].select_on_title(current_app.config['SEARCH_TITLE']):
            return render_template('books.html',books = current_app.config['VIEW_SEARCH'].select_on_title(str.lower(current_app.config['SEARCH_TITLE'] )), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'search', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])      
        else:
             print(f'Книги c похожим названием отсутствуют отсутствуют')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR']) 
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html') 
    
@search_filter.route('/<login>/filter/page/<int:page>', methods = ['POST', 'GET'])
def filter(login: str, page: int) -> render_template:
    """Эта функция возвращает все найденные книжные издания по фильтру

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Переменные:
        :year (int): Заданный год
        :tag (str): Заданный тэг
        :language (str): Заданный язык

    Параметры для render_template:
        :books (ViewFilter): Модель представления базы данных filter \n
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
        :books.html : Возвращает страницу с книгами если сессия работы с библиотекой  не завершена \n
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранным статусом \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    
    Результаты выполнения условий подоготовки фильтра (аналогично для двух других блоков условий):
        :if page == 1: FILTER_YEAR, FILTER_LANGUAGE и FILTER_TAG сбрасываются
        :if ['FILTER_YEAR'] == None: Присвоение переменной значения
        :elif ('year') and ('year') ! = ['FILTER_YEAR']:  Присвоение переменной значения

    Результаты выполнения условий фильтра:
        :if year and language and tag: Возвращает страницу с книгами по трем критериям (год, язык и тэг) \n
        :elif tag and year: Возвращает страницу с книгами по двум критериям (тэг и год) \n
        :elif tag and language: Возвращает страницу с книгами по двум критериям (тэг и язык) \n
        :elif language and year: Возвращает страницу с книгами по двум критериям (язык и год) \n
        :elif tag: Возвращает страницу с книгами по одному критерию (тэг) \n
        :elif language: Возвращает страницу с книгами по одному критерию (язык) \n
        :elif year: Возвращает страницу с книгами по одному критерию (год) \n
    """
    if page == 1:
        current_app.config['FILTER_YEAR'] = None
        current_app.config['FILTER_LANGUAGE'] = None
        current_app.config['FILTER_TAG'] = None
        
    if current_app.config['FILTER_YEAR'] == None:
        current_app.config['FILTER_YEAR'] = request.form.get('year')
    elif request.form.get('year')  and request.form.get('year') != current_app.config['FILTER_YEAR']:
        current_app.config['FILTER_YEAR'] = request.form.get('year')
    
    if current_app.config['FILTER_LANGUAGE'] == None:
        current_app.config['FILTER_LANGUAGE'] = request.form.get('language')
    elif request.form.get('language')  and request.form.get('language') != current_app.config['FILTER_LANGUAGE']:
        current_app.config['FILTER_LANGUAGE'] = request.form.get('language')

    if current_app.config['FILTER_TAG'] == None:
        current_app.config['FILTER_TAG'] = request.form.get('tag')
    elif request.form.get('tag')  and request.form.get('tag') != current_app.config['FILTER_TAG']:
        current_app.config['FILTER_TAG'] = request.form.get('tag')

    year = current_app.config['FILTER_YEAR']
    language = current_app.config['FILTER_LANGUAGE']
    tag = current_app.config['FILTER_TAG']

    

    if year:
        if request.form.get('year') == 'Выберите год издания' or not request.form.get('year'):
            year = current_app.config['FILTER_YEAR']
        else:
            year = request.form.get('year') 
            if year != current_app.config['FILTER_YEAR']:
                current_app.config['FILTER_YEAR'] = year
    else:
        year = request.form.get('year') 
        current_app.config['FILTER_YEAR'] = request.form.get('year') 


    if current_app.config['USER_LOGIN']:
        #выбраны все критерии
        if year and language and tag:
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_all('%' + tag + '%', year  + '%', '%' + language  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])      
        #выбран тэг и год
        elif tag and year:
            current_app.config['FILTER_LANGUAGE'] = None
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_tag_year('%' + tag + '%', '%' +  year  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])  
        #выбран тэг и язык+
        elif tag and language:
            current_app.config['FILTER_LANGUAGE'] = None
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_tag_language('%' + tag + '%', '%' + language  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])  
        #выбран язык и год+
        elif language and year:
            current_app.config['FILTER_TAG'] = None
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_year_language('%' + language  + '%', '%' +  year  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])  
        #выбран тэг+
        elif tag:
            current_app.config['FILTER_LANGUAGE'] = None
            current_app.config['FILTER_YEAR'] = None
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_tag('%' + tag + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])          
        #выбран язык
        elif language:
            current_app.config['FILTER_TAG'] = None
            current_app.config['FILTER_YEAR'] = None
            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_language('%' + language  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])          
        #выбран год
        elif year:

            return render_template('books.html',books = current_app.config['VIEW_FILTER'].select_for_filter_year('%' +  year  + '%'), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'filter', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])          
        else:
             print(f'Книги c похожим названием отсутствуют отсутствуют')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR']) 
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html') 
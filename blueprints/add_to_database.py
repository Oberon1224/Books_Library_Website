from flask import Blueprint, render_template, current_app, request
from .function import formation_authors, formation_tags, parser_html_ajax, parser_list_in_list

add_to_database = Blueprint('add_to_database', __name__, template_folder='templates')

@add_to_database.route('/add_new_tag', methods = ['POST', 'GET'])
def add_new_tag() -> None:
    """Запрос добавления нового тэга в базу данных

    Переменные:
        :tag (str): Новый тэг

    Результаты выполнения условий:
        :if not current_app.config: выполняется запрос insert \n
        :else: ничего не выполняется

    Returns:
        :str: Возвращает пустую строку
    """    
    tag = request.form.get('tag')
    if tag:
        if not current_app.config['TAG'].select_id_on_tag(tag):
            current_app.config['TAG'].insert_get_data(tag)
            print(f"Тэг с названием '{tag}' добавлен в базу данных!")
        else:
            print(f"Тэг с названием '{tag}' уже имется в базе данных!")
    return 'None'

@add_to_database.route('/add_new_author', methods = ['POST', 'GET'])
def add_new_author() -> None:
    """Запрос добавления нового автора в базу данных

    Переменные:
        :surname (str): Фамилия нового автора \n
        :name (str): Имя нового автора \n
        :patronymic (str): Отчество нового автора

    Результаты выполнения условий:
        if not current_app.config: выполняется запрос insert \n
        else: ничего не выполняется

    Returns:
        str: Возвращает пустую строку
    """ 
    surname = request.form.get('surname')
    name = request.form.get('name')
    patronymic = request.form.get('patronymic')
    if surname and name and patronymic:
        if not current_app.config['AUTHOR'].select_on_full_name(surname, name, patronymic):
            current_app.config['AUTHOR'].insert_get_data(surname, name, patronymic)
            print(f"Автор с имененм '{surname} {name} {patronymic}' добавлен в базу данных!")
        else:
            print(f"Автор с имененм '{surname} {name} {patronymic}' уже имеется в базе данных!")
    return 'None'

@add_to_database.route('/add_file', methods = ['POST', 'GET'])
def add_file() -> None:
    """Запрос добавления книги в базу данных. 
    В данной функции выполняется многоуровневая проверка каждой переменной с выполнением
    запросов добавления согласно связям между таблицами базами данных.
    Сначала выполняется добавление книги с необходимой для нее информации,
    затем выполняется добавление списков авторов и тэгов с заранне подоготовленными данными 
    для добавления.

    Переменные:
        :title (str): Название новой книги \n
        :page (str): Имя нового автора \n
        :path_book (str): Отчество нового автора \n
        :path_image (str): Отчество нового автора \n
        :category (str): Отчество нового автора \n
        :language (str): Отчество нового автора \n
        :year (str): Отчество нового автора \n
        :authors (list[str]): Список авторов для новой книги \n
        :tags (list[str]): Список тэгов для новой книги 

    Returns:
        :str: Возвращает пустую строку
    """ 

    title = request.form.get('title')
    page = request.form.get('page')
    path_book = request.form.get('path_book')
    path_image = request.form.get('path_image')
    category= request.form.get('category')
    language = request.form.get('language')
    year = request.form.get('year')
    authors = formation_authors(parser_html_ajax('authors'))
    tags = formation_tags(parser_html_ajax('tags'))
    description = request.form.get('description')
    if title and  page and  path_book and category and language and authors and tags and description:
        id_year = current_app.config['YEAR'].select_id_by_year(year)[0][0]
        id_language = current_app.config['LANGUAGE'].select_id_by_language(language)[0][0]
        id_book = current_app.config['BOOK'].get_last_row()
        id_about = current_app.config['ABOUT'].get_last_row()
        current_app.config['ABOUT'].insert_get_date(description, id_book)
        id_category = current_app.config['CATEGORY'].select_id_by_category(category)[0][0]
        if id_year and id_language and id_about and id_category:
            current_app.config['BOOK'].insert_get_data(title, page, path_book, path_image, int(id_year),
                                                        int(id_language), int(id_about), int(id_category))
            id_authors = list()
            id_tags = list()
            if id_book:
                for k in authors:
                    id_authors.append(current_app.config['AUTHOR'].select_on_full_name(k[0], k[1], k[2]))
                id_authors = parser_list_in_list(id_authors)
                for k in tags:
                    id_tags.append(current_app.config['TAG'].select_id_on_tag(k[0]))
                id_tags = parser_list_in_list(id_tags)
                if id_authors:
                    for k in id_authors:
                        current_app.config['LIST_AUTHORS'].insert_get_date(k, id_book)
                        print(f'Автор с id = {k} добавлен в книгу с id = {id_book}!')
                else:
                    print('Список id авторов пуст!')
                if id_tags:
                    for k in id_tags:
                        current_app.config['LIST_TAGS'].insert_get_date(k, id_book)
                        print(f'Тэг с id = {k} добавлен в книгу с id = {id_book}!')
                else:
                    print('Список id тэгов пуст!')                        
            else:
                print('ID книги пуст!')
        else:
            print('Не все списки id заполнены!')
    else:
        print("Не все поля заполнены!")
    return 'None'

@add_to_database.route('/change_add_author', methods = ['POST', 'GET'])
def change_add_author() -> None:
    """Запрос добавления автора/авторов к книге. 
    В данной функции выполняется многоуровневая проверка каждой переменной,
    формируется список для добавления и затем выполняется запрос insert.

    Переменные:
        :id_book (str): Фамилия нового автора \n
        :authors (str): Список авторов

    Returns:
        :str: Возвращает пустую строку
    """ 
    id_book = request.form.get('id_book')
    authors = formation_authors(parser_html_ajax('authors'))
    if id_book and authors:
        id_authors = list()
        for k in authors:
            id_authors.append(current_app.config['AUTHOR'].select_on_full_name(k[0], k[1], k[2]))
        id_authors = parser_list_in_list(id_authors)
        if id_authors:
            for k in id_authors:
                if not current_app.config['LIST_AUTHORS'].select_on_id_book_and_author(k, id_book):
                    current_app.config['LIST_AUTHORS'].insert_get_date(k, id_book)    
                    print(f'Автор с ID = {k} добавлен в книгу с ID = {id_book}')
                else:
                    print(f'Автор с ID = {k} уже имеется в книге с ID = {id_book}')
        else:
            print('Список id авторов пуст!')
    else:
        print('Отсутствуют авторы или id книги!')
    return 'None'

@add_to_database.route('/change_add_tag', methods = ['POST', 'GET'])
def change_add_tag():
    """Запрос добавления тэга/тэгов к книге. 
    В данной функции выполняется многоуровневая проверка каждой переменной,
    формируется список для добавления и затем выполняется запрос insert.

    Переменные:
        :id_book (str): Фамилия нового автора \n
        :tags (str): Список тэгов

    Returns:
        :str: Возвращает пустую строку
    """ 
    id_book = request.form.get('id_book')
    tags = formation_tags(parser_html_ajax('tags'))
    if id_book and tags:
        id_tags = list()
        for k in tags:
            id_tags.append(current_app.config['TAG'].select_id_on_tag(k[0]))
        id_tags = parser_list_in_list(id_tags)
        if id_tags:
            for k in id_tags:
                if not current_app.config['LIST_TAGS'].select_on_id_book_and_tag(k, id_book):
                    current_app.config['LIST_TAGS'].insert_get_date(k, id_book)  
                    print(f'Тэг с ID = {k} добавлен в книгу с ID = {id_book}')
                else:
                    print(f'Тэг с ID = {k} уже имеется в книге с ID = {id_book}')
        else:
            print('Список id тэгов пуст!')
    else:
        print('Отсутствуют тэги или id книги!')
    return 'None'

@add_to_database.route('/<login>/add', methods = ['POST', 'GET'])
def add(login: str) -> render_template:
    """Переход на страницу добавления книги.

    Args:
        login (string): Имя пользователя

    Результаты выполнения условий:
        :if current_app.config: Переход на страницу add_file.html \n
        :else: Переход на страницу index.html

    Returns:
        :render_template: Страница html

    Возвращаемые html страницы:
        :add_file.html: Возвращает страницу добавления книги если сессия работы с библиотекой  не завершена \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """ 
    if current_app.config['USER_LOGIN']:
        return render_template('add_file.html',login = login, style = current_app.config['STYLE'],
                               tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                               year = current_app.config['YEAR'], category = current_app.config['CATEGORY'], 
                               book = current_app.config['BOOK'], author = current_app.config['AUTHOR'])   
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  
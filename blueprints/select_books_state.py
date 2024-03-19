from flask import Blueprint, render_template, current_app

select_books_state = Blueprint('select_books_state', __name__, template_folder = 'templates')

@select_books_state.route('/<login>/on_reading/page/<int:page>', methods = ['POST', 'GET'])
def on_reading(login: str, page: int) -> render_template:
    """Эта функция возвращает все категории книжных изданий со статустом "На чтении"

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewInRead): Модель представления базы данных view_in_read \n
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
    if (current_app.config['USER_LOGIN']):
        if (current_app.config['VIEW_IN_READ'].select_for_user(login)):
            return render_template('books.html',books = current_app.config['VIEW_IN_READ'].select_for_user(login), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'on_reading', state = current_app.config['STATE'], 
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])   
        else:
             print(f'Книги на чтении у пользователя с логином {login} отсутствуют')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR']) 
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@select_books_state.route('/<login>/favorites/page/<int:page>', methods = ['POST', 'GET'])
def favorites(login: str, page: int) -> render_template:
    """Эта функция возвращает все категории книжных изданий со статустом "Избранное"

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewFavorites): Модель представления базы данных view_favorites \n
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
    if(current_app.config['USER_LOGIN']):
        if(current_app.config['VIEW_FAVORITES'].select_for_user(login)):
            return render_template('books.html', books = current_app.config['VIEW_FAVORITES'].select_for_user(login), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'favorites', state = current_app.config['STATE'], 
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])   
        else:
             print(f'Книги в избранном у пользователя с логином {login} отсутствуют')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR'])

    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@select_books_state.route('/<login>/end_read/page/<int:page>', methods = ['POST', 'GET'])
def end_read(login: str, page: int) -> render_template:
    """Эта функция возвращает все категории книжных изданий со статустом "Прочитанное"

    Args:
        login (string): Имя пользователя
        page (int): Страница
        
    Параметры для render_template:
        :books (ViewEndRead): Модель представления базы данных view_end_read \n
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
        render_template: Страница html

    Возвращаемые html страницы:
        :books.html: Возвращает страницу с книгами если сессия работы с библиотекой  не завершена \n
        :main.html: Возвращает главную страницу если у пользователя отсутствуют книги с выбранным статусом \n
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n
    """    
    if (current_app.config['USER_LOGIN']):
        if (current_app.config['VIEW_END_READ'].select_for_user(login)):
            return render_template('books.html', books = current_app.config['VIEW_END_READ'].select_for_user(login), 
                                    page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], authors = current_app.config['AUTHOR'],
                                    language = current_app.config['LANGUAGE'], year = current_app.config['YEAR'],
                                    category = 'end_read', state = current_app.config['STATE'],
                                    id_user = (current_app.config['USER'].select_id_on_login(current_app.config['USER_LOGIN']))[0][0])   
        else:
             print(f'Книги в избранном у пользователя с логином {login} отсутствуют')
             return render_template('main.html', page = page, login = login, style = current_app.config['STYLE'],
                                    tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                                    year = current_app.config['YEAR']) 
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  
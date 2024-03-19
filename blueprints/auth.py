#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, render_template, current_app, request

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/exit', methods = ['POST', 'GET'])
def exit() -> render_template:
    """Выход из личного кабинета

    Переменные:
        :current_app.config['USER_LOGIN']  (str): имя пользователя

    Returns:
        :render_template:  Страница html

    Возвращаемые html страницы:
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n        
    """ 
    print('Завершение сессии работы с библиотекой')
    current_app.config['USER_LOGIN'] = None
    return render_template('index.html')  

@auth.route('/main', methods = ['POST', 'GET'])
def main() -> render_template:
    """Переход на главную страницу

    Переменные:
        :current_app.config['USER_LOGIN'] (str): имя пользователя
        :login_enter (str): Введенный логин
        :password_enter (str): Введенный пароль
        :password_user (str): Пароль пользователя из базы данных

    Параметры для render_template:
        :login (str): Логин пользователя \n
        :style (str): Стиль приложения \n
        :tags (Tag): Модель таблицы базы данных tag \n
        :language (Language): Модель таблицы базы данных language \n
        :year (Year): Модель таблицы базы данных year \n

    Результаты выполнения условий:
        :if login_enter and password_enter and 
        current_app.config['USER'].select_password_on_login(login_enter): Выборка пароля из базы данных для пользователя \n
        :if password_user: Допуск к следующей проверки
        :if password_user == password_enter: Сохранение логина в переменной приложения
        :if current_app.config['USER_LOGIN']: Переход на страницу main.html
        :else: Переход на страницу index.html

    Returns:
        :render_template:  Страница html

    Возвращаемые html страницы:
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n        
    """ 
    if not current_app.config['USER_LOGIN']:
        login_enter = request.form.get('login_user')
        password_enter = request.form.get('password_user')
        if login_enter and password_enter and current_app.config['USER'].select_password_on_login(login_enter):
            password_user = current_app.config['USER'].select_password_on_login(login_enter)[0][0]
            if password_user:
                if password_user == password_enter:
                    current_app.config['USER_LOGIN'] = login_enter
                else:
                    print('Неверный пароль!')
            else:
                print('Пользователя с таким логином нету в базе данных!')
        else:
            print('Логин или пароль не введены!') 
    if current_app.config['USER_LOGIN']:
        return render_template('main.html', login = current_app.config['USER_LOGIN'], style = current_app.config['STYLE'],
                               tags = current_app.config['TAG'], language = current_app.config['LANGUAGE'], 
                               year = current_app.config['YEAR'])
    else:
        print('Завершение сессии работы с библиотекой')
        return render_template('index.html')  

@auth.route('/')
def index() -> render_template:
    """Переход на страницу авторизации

    Returns:
        :render_template:  Страница html

    Возвращаемые html страницы:
        :index.html: Возвращает страницу авторизации если сессия работы с библиотекой прервана \n        
    """ 
    return render_template('index.html')  


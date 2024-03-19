#Copyright 2024 Bushuev Dmitrii

from flask import Blueprint, current_app

style = Blueprint('style', __name__, template_folder = 'templates')

@style.route('/style1', methods = ['POST', 'GET'])
def style1() -> str:
    """Эта функция меняет стиль страницы

    Returns:
        str: Изменение стиля
    """    
    print('style1')
    current_app.config['STYLE'] = 'style1'
    print('Установлен стиль 1')
    return 'style1'

@style.route('/style2', methods = ['POST', 'GET'])
def style2() -> str:
    """Эта функция меняет стиль страницы

    Returns:
        str: Изменение стиля
    """
    print('style2')
    current_app.config['STYLE'] = 'style2'
    print('Установлен стиль 2')
    return 'style2'

@style.route('/style3', methods = ['POST', 'GET'])
def style3() -> str:
    """Эта функция меняет стиль страницы

    Returns:
        str: Изменение стиля
    """
    print('style3')
    current_app.config['STYLE'] = 'style3'
    print('Установлен стиль 3')
    return 'style3'

@style.route('/style4', methods = ['POST', 'GET'])
def style4() -> str:
    """Эта функция меняет стиль страницы

    Returns:
        str: Изменение стиля
    """
    print('style4')
    current_app.config['STYLE'] = 'style4'
    print('Установлен стиль 4')
    return 'style4'

@style.route('/style5', methods = ['POST', 'GET'])
def style5() -> str:
    """Эта функция меняет стиль страницы
    
    Returns:
        str: Изменение стиля
    """
    print('style5')
    current_app.config['STYLE'] = 'style5'
    print('Установлен стиль 5')
    return 'style5'
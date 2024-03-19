import re
from flask import request

def check_book_on_user(books_by_user: list[str], book_in_check: str) -> bool:
    """Эта функция проверяет наличие книги у пользователя
    
    Args:
        books_by_user (list[str]): Список книг автора
        book_in_check (str): Книга сравниваемая с книгами пользователя

    Variable:
        :param check (bool): Переменная проверки книги, check = False, если книга имеется у пользователя check = True

    Returns:
        :bool: True - книга имеется у пользователя, False - книга отсутствует у пользователя
    """
    check = False
    for b in books_by_user:
        if str(b[0]) == str(book_in_check):
            check = True
            return check
    return check

def parser_html_ajax(id_container: int) -> re.findall:
    """Эта функция парсинга данных принятых с ajax в виде html в список строк

    Args:
        id_container (int): id контейнера данных html
    
    Functions:
        :function re.findall(): - Регулярное выражение с правилом '(?<=>)[^<>]+(?=</)', выбирающем текст внутри тегов html
        
    Returns:
        :re.findall: Список строк сформированный с помощью регулярных выражений
    """
    return re.findall(r'(?<=>)[^<>]+(?=</)', str(request.form.getlist(id_container)))

def formation_authors(list_words: list[str]) -> list[str]:
    """Эта функция формирует список авторов из списка слов ([Фамилия имя отчество] -> [Фамилия, Имя, Отчество] )

    Args:
        list_words (list[str]): Список слов

    Returns:
        :list[str]: Список авторов
    """
    list_authors = list()
    for k in list_words:
        list_authors.append(re.split(r'\W+', k))
    return list_authors

def formation_tags(list_words: list[str]) -> list[str]:
    """Эта функция формирует список тэгов из списка слов ([Тэг Тэг] -> [Тэг, Тэг] )

    Args:
        list_words (list[str]): Список слов

    Returns:
        :list[str]: Список тэгов
    """    
    list_tags = list()
    for k in list_words:
        list_tags.append([k])
    return list_tags

def parser_list_in_list(list_in_list: list[list[list[str]]]) -> list[list[str]]:
    """Эта функция уменьшат на один уровень вложенности списка
    Args:
        list_in_list (list[list[str]]): Многоуровневый список(больше трех уровне)

    Returns:
        :list [list[str]]: Список с уменьшенным количеством уровней и уникальными строками
    """    
    new_list = list()
    for k in range(len(list_in_list)):
        new_list.append(list_in_list[k][0][0])
    return(list(set(new_list)))

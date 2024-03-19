#Запрос создания таблицы author
query_create = """
    CREATE TABLE IF NOT EXISTS author
    (id_author INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    surname TEXTNULL,
    name TEXT NULL,
    patronymic TEXT NULL);
"""
#Запрос добавления данных в таблицу author
query_insert = "INSERT INTO author(name, surname, patronymic) VALUES (?, ?, ?);" 

#Запрос выборки всех записей из таблицы author
query_select_all = "SELECT * FROM author;"

#Запрос выборки фио автора по id книги
query_select_on_id_book = """
    SELECT author.surname || ' ' || author.name || ' ' || author.patronymic AS fio FROM author 
    INNER JOIN list_authors ON author.id_author = list_authors.id_author
    INNER JOIN book ON list_authors.id_book = book.id_book
    WHERE book.id_book = ?;
"""

#Запрос выборки id автора по фио автора
query_select_on_full_name = """
    SELECT id_author FROM author WHERE surname = ? AND name = ? AND patronymic = ?;
"""
#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы list_authors
query_create = """
    CREATE TABLE IF NOT EXISTS list_authors
    (id_list_authors INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_author INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    FOREIGN KEY(id_book) REFERENCES books(id_book),
    FOREIGN KEY(id_author) REFERENCES author(id_author));
"""

#Запрос добавления данных в таблицу list_authors
query_insert = "INSERT INTO list_authors(id_author, id_book) VALUES (?, ?);" 

#Запрос выборки всех записей из таблицы list_authors
query_select_all = "SELECT * FROM list_authors;"

#Запрос выборки id списка по id автора и id книги из таблицы list_authors
query_select_on_id_book_and_author = "SELECT id_list_authors FROM list_authors WHERE  id_author = ? AND id_book = ?;"
#Запрос создания таблицы tag
query_create = """
    CREATE TABLE IF NOT EXISTS tag
    (id_tag INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    tag_name TEXT NULL);
"""
#Запрос добавления данных в таблицу tag
query_insert = "INSERT INTO tag(tag_name) VALUES (?);" 

#Запрос выборки всех записей из таблицы tag
query_select_all = "SELECT * FROM tag;"

#Запрос выборки списка тэгов для книги по id книги
query_select_on_id_book = """
    SELECT tag_name FROM tag 
    INNER JOIN list_tags ON tag.id_tag = list_tags.id_tag
    INNER JOIN book ON list_tags.id_book = book.id_book
    WHERE book.id_book = ?;
"""

#Запрос выборки id тэга по названию тэга
query_select_id_on_tag = """
    SELECT id_tag FROM tag WHERE tag_name = ?;
"""
#Запрос создания таблицы language
query_create = """
    CREATE TABLE IF NOT EXISTS language
    (id_language INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name TEXT NULL);
"""
#Запрос добавления данных в таблицу language
query_insert = "INSERT INTO language(name) VALUES (?);" 

#Запрос выборки всех записей из таблицы language
query_select_all = "SELECT * FROM language;"

#Запрос выборки id языка по названию языку из таблицы language
query_select_id_by_language = "SELECT id_language FROM language WHERE name = ?"
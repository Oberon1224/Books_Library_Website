#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы category
query_create = """
    CREATE TABLE IF NOT EXISTS category
    (id_category INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    name TEXT NULL);
"""
#Запрос добавления данных в таблицу category
query_insert = "INSERT INTO category(name) VALUES (?);" 

#Запрос выборки всех записей из таблицы category
query_select_all = "SELECT * FROM category;"

#Запрос выборки id категории по названию категории из таблицы category
query_select_id_by_category = "SELECT id_category FROM category WHERE name = ?;"
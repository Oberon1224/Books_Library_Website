#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы state
query_create="""
    CREATE TABLE IF NOT EXISTS state
    (id_state INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    state_name TEXT NULL);
"""
#Запрос добавления данных в таблицу state
query_insert="INSERT INTO state(state_name) VALUES (?);"

#Запрос выборки всех записей из таблицы state
query_select_all = "SELECT * FROM state;"
 
#Запрос выборки статуса книги для пользователя
query_select_state_name = """
    SELECT state_name FROM state WHERE id_state 
    IN (SELECT id_state FROM list_states WHERE id_user = ? AND id_book = ?);
"""
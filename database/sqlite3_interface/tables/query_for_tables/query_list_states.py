#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы list_states
query_create = """
    CREATE TABLE IF NOT EXISTS list_states
    (id_list_states INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    page INTEGER NULL,
    id_state INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    FOREIGN KEY(id_book) REFERENCES book(id_book),
    FOREIGN KEY(id_user) REFERENCES user(id_user),
    FOREIGN KEY(id_state) REFERENCES state(id_state));
"""
#Запрос добавления данных в таблицу list_states
query_insert = """
    INSERT INTO list_states(page, id_state, id_book, id_user)
    VALUES (?, ?, ?, ?);
"""

#Запрос выборки страницы для закладки по id книги и id пользователя
query_select_state_page = "SELECT page FROM list_states WHERE id_book = ? and id_user = ?;"

#Запрос выборки всех записей из таблицы list_states
query_select_all = "SELECT * FROM list_states;"

#Запрос изменения статуса книги
query_update_state = """UPDATE list_states SET id_state = ? WHERE id_book = ? AND id_user = ?;"""

#Запрос изменения страницы закладки книги
query_update_state_page = "UPDATE list_states SET page = ? WHERE id_book = ? AND id_user = ?;"

#Запрос выборки книг пользователя
query_select_user_books = """
    SELECT id_book FROM list_states 
    INNER JOIN user ON list_states.id_user  = user.id_user
    INNER JOIN state ON state.id_state = list_states.id_state
    WHERE user.login = ?;
"""



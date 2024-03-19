#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы list_notes
query_create = """
    CREATE TABLE IF NOT EXISTS list_notes
    (id_list_notes INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_note INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    FOREIGN KEY(id_book) REFERENCES book(id_book),
    FOREIGN KEY(id_user) REFERENCES user(id_user),
    FOREIGN KEY(id_note) REFERENCES note(id_note));
"""

#Запрос добавления данных в таблицу list_notes
query_insert = "INSERT INTO list_notes(id_note, id_book, id_user) VALUES (?, ?, ?);" 

#Запрос выборки всех записей из таблицы list_notes
query_select_all = "SELECT * FROM list_notes;"



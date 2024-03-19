#Copyright 2024 Bushuev Dmitrii

#Запрос создания таблицы note
query_create = """
    CREATE TABLE IF NOT EXISTS note
    (id_note INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
    text_note TEXT NULL);
"""

#Запрос добавления данных в таблицу note
query_insert = "INSERT INTO note(text_note) VALUES (?);" 

#Запрос выборки всех записей из таблицы note
query_select_all = "SELECT * FROM note;"

#Запрос выборки заметок для книги по id книги
query_select_on_id_book = """
    SELECT note.id_note, note.text_note FROM note
    INNER JOIN list_notes ON list_notes.id_note = note.id_note
    INNER JOIN book ON list_notes.id_book = book.id_book
    WHERE book.id_book = ?;
"""

#Получегие id последней записи таблицы note
query_last_row = "SELECT id_note FROM note ORDER BY id_note DESC;"

#Запрос выборки заметок для книги для заданного пользователя
query_select_on_id_user_book = """
    SELECT * FROM note WHERE id_note IN 
    (SELECT id_note FROM list_notes WHERE id_book = ? AND id_user = ?);
"""
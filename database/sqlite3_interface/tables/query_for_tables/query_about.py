#Запрос создания таблицы about
query_create = """
    CREATE TABLE IF NOT EXISTS about
    (id_about INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    information TEXT NULL,
    id_book INTEGER NOT NULL,
    FOREIGN KEY(id_book) REFERENCES book(id_book));
"""

#Запрос добавления данных в таблицу about
query_insert = "INSERT INTO about(information, id_book) VALUES (?, ?);" 

#Запрос выборки всех записей из таблицы about
query_select_all = "SELECT * FROM about;"

#Запрос выборки последней записи в таблице about
query_last_row = "SELECT id_about FROM about ORDER BY id_about DESC;"

#Запрос выборки описания книги по id книги
query_select_information_by_book = "SELECT information FROM about WHERE id_book = ?;"

#Запрос изменения описания книги
query_update_information = "UPDATE about SET information = ? WHERE id_book = ?;"

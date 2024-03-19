#Запрос создания таблицы book
query_create = """
    CREATE TABLE IF NOT EXISTS book 
    (id_book INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    title TEXT NOT NULL,
    page INTEGER NULL,
    path_book TEXT NULL,
    path_image TEXT NULL,
    id_year INTEGER,
    id_language INTEGER,
    id_about INTEGER,
    id_category INTEGER,
    FOREIGN KEY (id_year) REFERENCES year(id_year),
    FOREIGN KEY (id_language) REFERENCES language(id_language),
    FOREIGN KEY (id_about) REFERENCES about(id_about),
    FOREIGN KEY (id_category) REFERENCES category(id_category));
"""
#Запрос добавления данных в таблицу book
query_insert = """
    INSERT INTO book (title,page, path_book, path_image,id_year,id_language,id_about,id_category)
    VALUES(?,?,?,?,?,?,?,?);
""" 

#Запрос выборки последней записи таблицы book
query_last_row ="SELECT id_book FROM book ORDER BY id_book DESC;"

#Запрос выборки пути к файлу книги по id книги
query_select_path_book = "SELECT path_book FROM book WHERE id_book = ?;"

#Запрос выборки всех записей из таблицы book
query_select_all = "SELECT * FROM book;"

#Запрос выборки данных о книге по id книги
query_select_on_id_book = "SELECT title, page, path_book, path_image, id_category, id_language, id_year FROM book WHERE id_book = ?;"

#Запрос изменения названия книги
query_update_title = "UPDATE book SET title = ? WHERE id_book = ?;"

#Запрос изменения количества страниц книги
query_update_page = "UPDATE book SET page = ? WHERE id_book = ?;"

#Запрос изменения пути к файлу книги
query_update_path_book = "UPDATE book SET path_book = ? WHERE id_book = ?;"

#Запрос изменения пути к изображению книги
query_update_path_image = "UPDATE book SET path_image = ? WHERE id_book = ?;"

#Запрос изменения языка книги 
query_update_id_year = "UPDATE book SET id_year = (SELECT id_year FROM year WHERE year = ?)  WHERE id_book = ?;"

#Запрос изменения года издания книги
query_update_id_language = "UPDATE book SET id_language = (SELECT id_language FROM language WHERE name = ?)  WHERE id_book = ?;"

#Запрос изменения категории книги
query_update_id_category = "UPDATE book SET id_category = (SELECT id_category FROM category WHERE name = ?)  WHERE id_book = ?;"
#Запрос создания таблицы list_tags
query_create = """
    CREATE TABLE IF NOT EXISTS list_tags
    (id_list_tags INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    id_tag INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    FOREIGN KEY(id_book) REFERENCES book(id_book),
    FOREIGN KEY(id_tag) REFERENCES tag(id_tag));
"""

#Запрос добавления данных в таблицу list_tags
query_insert = "INSERT INTO list_tags(id_tag, id_book) VALUES (?, ?);" 

#Запрос выборки всех записей из таблицы list_tags
query_select_all = "SELECT * FROM list_tags;"

#Запрос выборки id по id книги и id тэгу
query_select_on_id_book_and_tag = "SELECT id_list_tags FROM list_tags WHERE  id_tag = ? AND id_book = ?; "
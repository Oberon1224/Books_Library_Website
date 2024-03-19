#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_list_tags import data_list_tags
from .query_for_tables.query_list_tags import query_create, query_insert, query_select_all, query_select_on_id_book_and_tag


class ListTags(Table):
    """ Класс является моделью таблицы list_tags.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы list_tags \n
            :self.query_insert (str): Запрос добавления данных в таблицу list_tags \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы list_tags \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы list_tags \n
            :self.query_select_on_id_book_and_tag (str): Запрос выборки id по id книги и id тэгу

        SQL-запрос создания таблицы list_tags (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS list_tags
                (id_list_tags INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                id_tag INTEGER NOT NULL,
                id_book INTEGER NOT NULL,
                FOREIGN KEY(id_book) REFERENCES book(id_book),
                FOREIGN KEY(id_tag) REFERENCES tag(id_tag));

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM list_tags;
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_list_tags
        self.query_select_all = query_select_all
        self.query_select_on_id_book_and_tag = query_select_on_id_book_and_tag

    def insert_get_date(self, id_tag: int, id_book: int) -> None:
        """Функция добавления данных в таблицу

            Args:
                id_tag (int): id тэга
                id_book (int): id книги

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO list_tags(id_tag, id_book) VALUES (?, ?);
        """               
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (id_tag, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()  
        except:
            print('Ошибка выполнения запроса insert_get_date в классе ListTags!')  

    def select_on_id_book_and_tag(self, id_tag: int, id_book: int) -> list[list[str]]:
        """Функция выборки id по id книги и id тэгу

            Args:
                id_tag (int): id тэга
                id_book (int): id книги

            SQL-запрос (self.query_select_on_id_book_and_tag): 
                ..  code-block:: sql

                    SELECT id_list_tags FROM list_tags 
                    WHERE  id_tag = ? AND id_book = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """              
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_id_book_and_tag, (id_tag, id_book))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
            print('Ошибка выполнения запроса select_on_id_book_and_tag в классе ListTags!')
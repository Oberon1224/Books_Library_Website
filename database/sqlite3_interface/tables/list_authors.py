from .table import Table
from .data_for_tables.data_list_authors import data_list_authors
from .query_for_tables.query_list_authors import query_create, query_insert, query_select_all, query_select_on_id_book_and_author

class ListAuthors(Table):
    """ Класс является моделью таблицы list_authors.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы list_authors \n
            :self.query_insert (str): Запрос добавления данных в таблицу list_authors \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы list_authors \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы list_authors \n
            :self.query_select_on_id_book_and_author (str): Запрос выборки id списка по id автора и id книги из таблицы list_authors 

        SQL-запрос создания таблицы list_authors (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS list_authors
                (id_list_authors INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                id_author INTEGER NOT NULL,
                id_book INTEGER NOT NULL,
                FOREIGN KEY(id_book) REFERENCES books(id_book),
                FOREIGN KEY(id_author) REFERENCES author(id_author));

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM list_authors;
    """   

    def __init__(self, name_db: str) -> None:
        super().__init__(name_db=name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_list_authors
        self.query_select_all = query_select_all
        self.query_select_on_id_book_and_author = query_select_on_id_book_and_author

    def insert_get_date(self, id_author: int, id_book: int) -> None:
        """Функция добавления данных в таблицу list_authors

            Args:
                id_author (int): id автора
                id_book (int): id книги

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO list_authors(id_author, id_book) 
                    VALUES (?, ?);
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (id_author, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса insert_get_date в классе ListAuthors!')   

    def select_on_id_book_and_author(self, id_author: int, id_book: int) -> list[list[str]]:
        """Функция выборки id списка по id автора и id книги из таблицы list_authors

            Args:
                id_author (int): id автора
                id_book (int): id книги

            SQL-запрос (self.query_select_on_id_book_and_author): 
                ..  code-block:: sql

                    SELECT id_list_authors FROM list_authors 
                    WHERE  id_author = ? AND id_book = ?
                    
            Returns:
                :list[list[str]]: Результат выборки
        """ 
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_id_book_and_author,(id_author, id_book))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
           print('Ошибка выполнения запроса select_on_id_book_and_author в классе ListAuthors!')   
#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_tag import data_tag
from .query_for_tables.query_tag import query_create, query_insert, query_select_all
from .query_for_tables.query_tag import query_select_on_id_book, query_select_id_on_tag

class Tag(Table):
    """ Класс является моделью таблицы tag.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы tag \n
            :self.query_insert (str): Запрос добавления данных в таблицу tag \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы tag \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы tag \n
            :self.query_select_on_id_book (str): Запрос выборки списка тэгов для книги по id книги \n
            :self.query_select_id_on_tag (str): Запрос выборки id тэга по названию тэга 

        SQL-запрос создания таблицы tag (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS tag
                (id_tag INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                tag_name TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO tag(tag_name) VALUES (?);

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM tag;
    """           
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_tag
        self.query_select_all = query_select_all
        self.query_select_on_id_book = query_select_on_id_book
        self.query_select_id_on_tag = query_select_id_on_tag

    def select_on_id_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки названия тэга по id книги

        Args:
            id_book (int): id книги

        SQL-запрос (self.query_select_on_id_book): 
            ..  code-block:: sql

                SELECT tag_name FROM tag 
                INNER JOIN list_tags ON tag.id_tag = list_tags.id_tag
                INNER JOIN book ON list_tags.id_book = book.id_book
                WHERE book.id_book = ?
            
        Returns:
            list[list[str]]: Результат выборки
        """        
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_id_book, (id_book,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results
        except:
            print('Ошибка выполнения запроса select_on_id_book в классе Tag!') 
    
    def select_id_on_tag(self, tag_name: str) -> list[list[str]]:
        """Функция выборки id тэга по названию тэга

        Args:
            tag_name (int): название тэга

        SQL-запрос (self.query_select_id_on_tag): 
            ..  code-block:: sql

                SELECT id_tag FROM tag WHERE tag_name = ?;
            
        Returns:
            list[list[str]]: Результат выборки
        """       
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_id_on_tag, (tag_name,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results
        except:
            print('Ошибка выполнения запроса select_id_on_tag в классе Tag!') 
                  
    def insert_get_data(self, tag_name: str) -> None:
        """Функция добавления тэга в базу данных

        Args:
            tag_name (int): название тэга

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO tag(tag_name) VALUES (?);
        """       
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (tag_name,))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса insert_get_data в классе Tag!') 
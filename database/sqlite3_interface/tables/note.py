#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_note import data_note
from .query_for_tables.query_note import query_create, query_insert, query_select_all
from .query_for_tables.query_note import query_select_on_id_book, query_last_row, query_select_on_id_user_book

class Note(Table):
    """ Класс является моделью таблицы note.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы note \n
            :self.query_insert (str): Запрос добавления данных в таблицу note \n
            :self.query_last_row (str): Получегие id последней записи таблицы note \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы note \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы note \n
            :self.query_select_on_id_book (str): Запрос выборки заметок для книги по id книги  \n
            :self.query_select_on_id_user_book (str): Запрос выборки заметок для книги для заданного пользователя  \n

        SQL-запрос создания таблицы note (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS note
                (id_note INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
                text_note TEXT NULL);

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM note;

        SQL-запрос (self.query_last_row): 
            ..  code-block:: sql

                SELECT id_note FROM note ORDER BY id_note DESC;

    """            
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.query_last_row = query_last_row
        self.data_to_db = data_note
        self.query_select_all = query_select_all
        self.query_select_on_id_book = query_select_on_id_book
        self.query_select_on_id_user_book = query_select_on_id_user_book

    def select_on_id_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки заметок для книги по id книги

            Args:
                id_book (int): id книги

            SQL-запрос (self.query_select_on_id_book): 
                ..  code-block:: sql

                    SELECT note.id_note, note.text_note FROM note
                    INNER JOIN list_notes ON list_notes.id_note = note.id_note
                    INNER JOIN book ON list_notes.id_book = book.id_book
                    WHERE book.id_book = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """               
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_id_book, (id_book,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results 
        except:
            print('Ошибка выполнения запроса select_on_id_book в классе Note!')           

    def insert_get_data(self, text_note: str) -> None:
        """Функция добавления заметки для книги

            Args:
                text_note (int): Текст заметки

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO note(text_note) VALUES (?);
        """              
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (text_note,))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса insert_get_data в классе Note!') 

    def select_on_id_user_book(self, id_book: int, id_user: int) -> list[list[str]]:
        """Функция выборки заметок для книги для заданного пользователя

            Args:
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_select_on_id_user_book): 
                ..  code-block:: sql

                    SELECT * FROM note WHERE id_note 
                    IN (SELECT id_note FROM list_notes 
                        WHERE id_book = ? AND id_user = ?); 
                    
            Returns:
                :list[list[str]]: Результат выборки
        """          
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_id_user_book, (id_book, id_user))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results 
        except:
           print('Ошибка выполнения запроса select_on_id_user_book в классе Note!')  
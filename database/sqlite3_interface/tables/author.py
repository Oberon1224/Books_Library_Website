from .table import Table
from .data_for_tables.data_author import data_author
from .query_for_tables.query_author import query_create, query_insert, query_select_all
from .query_for_tables.query_author import query_select_on_id_book, query_select_on_full_name

class Author(Table):
    """ Класс является моделью таблицы author.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы author \n
            :self.query_insert (str): Запрос добавления данных в таблицу author \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы author \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы author \n
            :self.query_select_on_id_book (str): Запрос выборки фио автора по id книги \n
            :self.query_select_on_full_name (str): Запрос выборки id автора по фио автора \n

        SQL-запрос создания таблицы book (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS author
                (id_author INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                surname TEXTNULL,
                name TEXT NULL,
                patronymic TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO author(name, surname, patronymic) VALUES (?, ?, ?);
                
        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM author;
    """        
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_author
        self.query_select_all = query_select_all
        self.query_select_on_id_book = query_select_on_id_book
        self.query_select_on_full_name = query_select_on_full_name

    def select_on_id_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки фио автора по id книги

            Args:
                id_book (int): id книги

            SQL-запрос (self.query_select_on_id_book): 
                ..  code-block:: sql

                    SELECT author.surname || ' ' || author.name 
                    || ' ' || author.patronymic AS fio FROM author 
                    INNER JOIN list_authors 
                    ON author.id_author = list_authors.id_author
                    INNER JOIN book 
                    ON list_authors.id_book = book.id_book 
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
            print('Ошибка выполнения запроса select_on_id_book в классе Author!') 
                
    def select_on_full_name(self, surname: str, name: str, patronymic: str) -> list[list[str]]:
        """Функция выборки id автора по фио автора

            Args:
                surname (str): Фамилия автора
                name (str): Имя автора
                patronymic (str): Отчество автора

            SQL-запрос (self.query_select_on_full_name): 
                ..  code-block:: sql

                    SELECT id_author FROM author 
                    WHERE surname = ? AND name = ? AND patronymic = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """         
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_full_name, (surname, name, patronymic))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results 
        except:
            print('Ошибка выполнения запроса select_on_full_name в классе Author!') 

    def insert_get_data(self, surname: str, name: str, patronymic: str) -> None:
        """Функция добавления данных в таблицу author

            Args:
                surname (str): Фамилия автора
                name (str): Имя автора
                patronymic (str): Отчество автора

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO author(name, surname, patronymic) 
                    VALUES (?, ?, ?);
                    
            Returns:
                :list[list[str]]: Результат выборки
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (name, surname, patronymic))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса insert_get_data в классе Author!')    
 
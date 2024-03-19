#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_list_states import data_list_states
from .query_for_tables.query_list_states import query_create, query_insert, query_select_all, query_select_state_page, query_select_user_books
from .query_for_tables.query_list_states import query_update_state_page, query_update_state

class ListStates(Table):
    """ Класс является моделью таблицы list_states.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы list_states \n
            :self.query_insert (str): Запрос добавления данных в таблицу list_states \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы list_states \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы list_states \n
            :self.query_select_state_page (str): Запрос выборки страницы для закладки по id книги и id пользователя \n
            :self.query_update_state_page (str): Запрос изменения страницы закладки книги \n
            :self.query_update_state (str): Запрос изменения статуса книги \n
            :self.query_select_user_books (str): Запрос выборки книг пользователя \n

        SQL-запрос создания таблицы list_states (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS list_states
                (id_list_states INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                page INTEGER NULL,
                id_state INTEGER NOT NULL,
                id_book INTEGER NOT NULL,
                id_user INTEGER NOT NULL,
                FOREIGN KEY(id_book) REFERENCES book(id_book),
                FOREIGN KEY(id_user) REFERENCES user(id_user),
                FOREIGN KEY(id_state) REFERENCES state(id_state));

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM list_states;
    """    

    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_list_states
        self.query_select_all = query_select_all
        self.query_select_state_page = query_select_state_page
        self.query_update_state_page = query_update_state_page
        self.query_update_state = query_update_state
        self.query_select_user_books = query_select_user_books

    def select_state_page(self, id_book: int, id_user: int) -> list[list[str]]:
        """Функция выборки страницы для закладки по id книги и id пользователя

            Args:
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_select_state_page): 
                ..  code-block:: sql

                    SELECT page FROM list_states 
                    WHERE id_book = ? and id_user = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """  
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_state_page, (id_book, id_user))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results
        except:
            print('Ошибка выполнения запроса select_state_page в классе ListStates!')  
    
    def select_user_books(self, login: str) -> list[list[str]]:
        """Функция выборки книг пользователя

            Args:
                login (int): Логин пользователя

            SQL-запрос (self.query_select_user_books): 
                ..  code-block:: sql

                    SELECT id_book FROM list_states 
                    INNER JOIN user ON list_states.id_user  = user.id_user
                    INNER JOIN state ON state.id_state = list_states.id_state
                    WHERE user.login = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """          
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_user_books, (login,))
            all_results=self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
            print('Ошибка выполнения запроса select_user_books в классе ListStates!')  

    def update_state(self, id_state: int, id_book: int, id_user: int) -> None:
        """Функция изменения статуса книги

            Args:
                id_state (int): id статуса книги
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_update_state): 
                ..  code-block:: sql

                    UPDATE list_states SET id_state = ? 
                    WHERE id_book = ? AND id_user = ?;
        """           
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_state, (id_state, id_book, id_user))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса update_state в классе ListStates!')  

    def insert_get_data(self, page: int, id_state: int, id_book: int, id_user: int) -> None:
        """Функция добавления данных в таблицу list_states

            Args:
                page (int): Номер страницы
                id_state (int): id статуса книги
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_update_state): 
                ..  code-block:: sql

                    INSERT INTO list_states(page, id_state, id_book, id_user) 
                    VALUES (?, ?, ?, ?);
        """          
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (page, id_state, id_book, id_user))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса insert_get_data в классе ListStates!')  

    def update_state_page(self, new_page: int, id_book: int, id_user: int) -> None:
        """Функция изменения страницы закладки книги

            Args:
                new_page (int): Новая страница
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_update_state_page): 
                ..  code-block:: sql

                    UPDATE list_states SET page = ? 
                    WHERE id_book = ? AND id_user = ?;
        """                     
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_state_page, (new_page, id_book, id_user))
            self.sqlite_connection.commit()
            self.close_connect_db()  
        except:
            print('Ошибка выполнения запроса update_state_page в классе ListStates!')     
    
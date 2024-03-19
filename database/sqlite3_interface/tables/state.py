#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_state import data_state
from .query_for_tables.query_state import query_create, query_insert
from .query_for_tables.query_state import query_select_all, query_select_state_name 

class State(Table): 
    """ Класс является моделью таблицы state.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы state \n
            :self.query_insert (str): Запрос добавления данных в таблицу state \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы state \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы state \n
            :self.query_select_state_name (str): Запрос выборки статуса книги для пользователя


        SQL-запрос создания таблицы state (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS state
                (id_state INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                state_name TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO state(state_name) VALUES (?);

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM state;
    """        
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_state
        self.query_select_all = query_select_all
        self.query_select_state_name = query_select_state_name
        
    def select_state_name(self, id_user: int, id_book: int) -> str:
        """Функция выборки статуса книги для пользователя

            Args:
                id_user (int): id пользователя
                id_book (int): id книги

            SQL-запрос (self.query_select_state_name): 
                ..  code-block:: sql

                    SELECT state_name FROM state WHERE id_state 
                    IN (SELECT id_state FROM list_states 
                        WHERE id_user = ? AND id_book = ?);
                    
            Returns:
                :state_name: Статус книги для пользователя
        """       
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_state_name, (id_user, id_book))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            if all_results:
                print(all_results[0][0])
                return all_results[0][0]
            else:
                return ' '
        except:
            print('Ошибка выполнения запроса select_state_name в классе State!') 
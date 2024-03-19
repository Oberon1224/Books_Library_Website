#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_user import data_user
from .query_for_tables.query_user import query_create, query_insert, query_select_all
from .query_for_tables.query_user import query_select_id_on_login, query_select_password_on_login 

class User(Table):
    """ Класс является моделью таблицы user.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы user \n
            :self.query_insert (str): Запрос добавления данных в таблицу user \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы user \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы user \n
            :self.query_select_id_on_login (str): Запрос выборки id пользователя с заданным логином \n
            :self.query_select_password_on_login (str): Запрос выборки пароля пользователя с заданным логином 


        SQL-запрос создания таблицы user (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS user
                (id_user INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                login TEXT NOT NULL,
                password TEXT NOT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO user(login, password) VALUES (?, ?);

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM user;
    """                
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_user
        self.query_select_all = query_select_all
        self.query_select_id_on_login = query_select_id_on_login
        self.query_select_password_on_login = query_select_password_on_login

    def select_id_on_login(self, login: str) -> list[list[str]]:
        """Функция получения id пользователя по логину пользователя

        Args:
            login (int): Логин пользователя

        SQL-запрос (self.query_select_id_on_login): 
            ..  code-block:: sql

                SELECT id_user FROM user WHERE login = ?;
            
        Returns:
            list[list[str]]: Результат выборки
        """        
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_id_on_login, (login,))
            all_results=self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
            print('Ошибка выполнения запроса select_id_on_login в классе User!') 

    def select_password_on_login(self, login: str) -> list[list[str]]:
        """Функция получения пароля пользователя по логину пользователя

        Args:
            login (int): Логин пользователя

        SQL-запрос (self.query_select_id_on_login): 
            ..  code-block:: sql

                SELECT password FROM user WHERE login = ?;
            
        Returns:
            list[list[str]]: Результат выборки
        """        
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_password_on_login, (login,))
            all_results=self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
            print('Ошибка выполнения запроса select_password_on_login в классе User!')             
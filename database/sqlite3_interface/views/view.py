#Copyright 2024 Bushuev Dmitrii


from abc import ABC, abstractmethod
import sqlite3

class View(ABC):
    """Абстрактный класс View - является моделью представления базы данных.

    Args:
        name_db (str): Имя базы данных

    Атрибуты:
        :self.name_db (str): Имя базы данных \n
        :self.sqlite_connection (sqlite3.Connection): Соединение с базой данных \n
        :self.cursor (sqlite3.Cursor): Курсор базы данных \n
        :self.create_query (str): Запрос создание представления \n
        :self.query_select_all (str): Запрос выборки всех записей из представления

    """       
    def __init__(self, name_db: str) -> None:     
        self.name_db: str = name_db
        self.sqlite_connection: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None
        self.create_query: str = None
        self.query_select_all: str = None

    def connect_db(self) -> None:
        """Функция выполняет соединение с базой данных.

        """   
        try:
            self.sqlite_connection=sqlite3.connect(self.name_db)
            self.cursor = self.sqlite_connection.cursor()
        except:
            print('Ошибка соединения с базой данных!')

    def close_connect_db(self) -> None:
        """Функция закрывает соединение с базой данных.

        """   
        try:
            self.sqlite_connection.close()
        except:
            print('Ошибка закрытия соединения с базой данных!')        

    def select_all(self) -> list[list[str]]:
        """Функция выполняет выборку всех записей из представления базы данных.

        Returns:
            list[list[str]]: Результат выборки
        """        
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_all)
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results    
        except:
            print('Ошибка выполнения запроса select_all!') 

    def create(self) -> None:
        """Функция выполняет запрос создания представления в базе данных.

        """  
        try:
            self.connect_db()
            cursor = self.sqlite_connection.cursor()
            cursor.execute(self.create_query)
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка создания представления!') 

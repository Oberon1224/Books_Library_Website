#Copyright 2024 Bushuev Dmitrii

from abc import ABC, abstractmethod
import sqlite3

class Table(ABC):
    """ Абстрактный класс Table - является моделью таблицы базы данных.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
        :self.name_db (str): Имя базы данных \n
        :self.sqlite_connection (sqlite3.Connection): Соединение с базой данных \n
        :self.cursor (sqlite3.Cursor): Курсор базы данных \n
        :self.create_query (str): Запрос создания таблицы \n
        :self.query_last_row (str): Запрос получения id последней записи таблицы \n
        :self.data_to_db (list[list[str]]): Тестовые данные для таблицы \n
        :self.query_insert (str): Запрос добавления данных в таблицу  \n
        :self.query_select_all (str): Запрос выборки всех записей из таблицы \n

    """               
    def __init__(self, name_db: str) -> None:
        self.name_db: str = name_db
        self.sqlite_connection: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None
        self.create_query: str = None
        self.query_last_row: str = None
        self.data_to_db: list[list] = None
        self.query_insert: str = None
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
            print('Ошибка выполнения запроса select_all в классе Table!') 
    
    def insert(self, *args: list[list]) -> None:
        """Функция Добавления тестовых данных в таблицу.
            Args:
                *args (list[list]): Список тестовых данных
        """  
        try:
            self.connect_db()
            self.cursor.executemany(self.query_insert, args)
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса insert в классе Table!') 

    def insert_data(self) -> None:
        """Функция подготовки тестовых данных перед добавлением в таблицу.

        """  
        try:
            for k in self.get_data_to_insert():
                data = list()
                for i in k:
                    data.append(i)
                print(data)
                self.insert(data)    
        except:
            print('Ошибка формирования данных для добавления в классе Table !') 
      
    def update(self, query: str) -> None:
        """Функция изменения информации в таблице.
            
            Args:
                query (str): SQS-запрос изменения информации в базе данных

        """  
        try:
            self.connect_db()
            self.cursor.execute(query)
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса update в классе Table!') 

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
            print('Ошибка выполнения запроса create в классе Table!')             
    
    def get_last_row(self) -> int:
        """Функция получения id последней записи таблицы.

            Returns:
                :int: id последней записи таблицы
        """  
        try:
            self.connect_db()
            self.cursor.execute(self.query_last_row)
            result = self.cursor.fetchone()
            self.close_connect_db()
            if result:
                return int(result[0]) + 1
            else:
                return 1
        except:
            print('Ошибка выполнения запроса get_last_row в классе Table!')   

    def get_data_to_insert(self) -> list[list]:
        """Функция получения тестовых данных.

            Returns:
                :list[list]: Тестовые данные
        """  
        return self.data_to_db
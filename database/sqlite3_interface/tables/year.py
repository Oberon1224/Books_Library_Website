#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_year import data_year
from .query_for_tables.query_year import query_create, query_insert, query_select_all, query_select_id_by_year

class Year(Table):
    """ Класс является моделью таблицы year.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы year \n
            :self.query_insert (str): Запрос добавления данных в таблицу year \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы year \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы year \n
            :self.query_select_id_by_year (str): Запрос выборки id года с заданным годом


        SQL-запрос создания таблицы year (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS year
                (id_year INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                year TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO year(year) VALUES (?);

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM year;
    """            
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_year
        self.query_select_all = query_select_all
        self.query_select_id_by_year = query_select_id_by_year

    def select_id_by_year(self, year: int) -> list[list[str]]:
        """Функция получения id года по заданному году

        Args:
            year (int): Год издания

        SQL-запрос (self.query_select_id_by_year): 
            ..  code-block:: sql

                SELECT id_year FROM year WHERE year = ?;
            
        Returns:
            list[list[str]]: Результат выборки
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_id_by_year, (year,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
           print('Ошибка выполнения запроса select_id_by_year в классе Year!') 
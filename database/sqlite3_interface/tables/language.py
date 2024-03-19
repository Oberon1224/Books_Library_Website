#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_language import data_language
from .query_for_tables.query_language import query_create, query_insert, query_select_all, query_select_id_by_language

class Language(Table):
    """ Класс является моделью таблицы language.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы language \n
            :self.query_insert (str): Запрос добавления данных в таблицу language \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы language \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы language \n
            :self.query_select_id_by_language (str): Запрос выборки id языка по названию языку из таблицы language

        SQL-запрос создания таблицы language (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS language
                (id_language INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                name TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO language(name) VALUES (?);
                
        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM language;
    """      
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_language
        self.query_select_all = query_select_all
        self.query_select_id_by_language = query_select_id_by_language

    def select_id_by_language(self, language: str) -> list[list[str]]:
        """Функция выборки id языка по названию языку из таблицы language

            Args:
                language (int): Название языка

            SQL-запрос (self.query_select_id_by_language): 
                ..  code-block:: sql

                    SELECT id_language FROM language 
                    WHERE name = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """ 
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_id_by_language, (language,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results
        except:
            print('Ошибка выполнения запроса select_id_by_language в классе Language!')           
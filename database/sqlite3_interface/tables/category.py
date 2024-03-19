from .table import Table
from .data_for_tables.data_category import data_category
from .query_for_tables.query_category import query_create, query_insert, query_select_all, query_select_id_by_category

class Category(Table):
    """ Класс является моделью таблицы category.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы category \n
            :self.query_insert (str): Запрос добавления данных в таблицу category \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы category \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы category \n
            :self.query_select_id_by_category (str): Запрос выборки id категории по названию категории из таблицы category

        SQL-запрос создания таблицы category (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS category
                (id_category INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                name TEXT NULL);

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO category(name) VALUES (?);
                
        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM category;
    """      
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_category
        self.query_select_all = query_select_all
        self.query_select_id_by_category = query_select_id_by_category

    def select_id_by_category(self, category: str) -> list[list[str]]:
        """Функция выборки id категории по названию категории из таблицы category

            Args:
                category (int): Название категории

            SQL-запрос (self.query_select_id_by_category): 
                ..  code-block:: sql

                    SELECT id_category FROM category 
                    WHERE name = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """ 
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_id_by_category, (category,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results  
        except:
            print('Ошибка выполнения запроса select_id_by_category в классе Category!') 
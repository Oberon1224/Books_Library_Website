from .table import Table
from .data_for_tables.data_about import data_about
from .query_for_tables.query_about import query_create, query_insert, query_select_all
from .query_for_tables.query_about import query_last_row, query_select_information_by_book
from .query_for_tables.query_about import query_update_information

class About(Table):
    """ Класс является моделью таблицы about.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы about \n
            :self.query_insert (str): Запрос добавления данных в таблицу about \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы about \n
            :self.query_last_row (str): Запрос выборки последней записи в таблице about \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы about \n
            :self.query_select_information_by_book (str): Запрос выборки описания книги по id книги \n
            :self.query_update_information (str): Запрос изменения описания книги

        SQL-запрос создания таблицы book (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS about
                (id_about INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                information TEXT NULL,
                id_book INTEGER NOT NULL,
                FOREIGN KEY(id_book) REFERENCES book(id_book));

        SQL-запрос (self.query_last_row): 
            ..  code-block:: sql

                SELECT id_about FROM about ORDER BY id_about DESC;
                
        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM about;
    """       
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_about
        self.query_select_all = query_select_all
        self.query_last_row = query_last_row
        self.query_select_information_by_book = query_select_information_by_book
        self.query_update_information = query_update_information

    def insert_get_date(self, description: str, id_book: int) -> None:
        """Функция добавления данных в таблицу about

            Args:
                description (str): Описание книги
                id_book (int): id id книги

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO about(information, id_book) 
                    VALUES (?, ?);
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (description, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса insert_get_date в классе About!') 

    def select_information_by_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки описания книги по id книги

            Args:
                id_book (int): id id книги

            SQL-запрос (self.query_select_information_by_book): 
                ..  code-block:: sql

                    SELECT information FROM about 
                    WHERE id_book = ?;

            Returns:
                :list[list[str]]: Результат выборки
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_information_by_book,(id_book,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results   
        except:
            print('Ошибка выполнения запроса select_information_by_book в классе About!') 

    def update_information(self, information: str, id_book: int) -> None:
        """Функция изменения описания книги

            Args:
                information (str): Описание книги
                id_book (int): id id книги

            SQL-запрос (self.query_update_information): 
                ..  code-block:: sql

                    UPDATE about SET information = ? 
                    WHERE id_book = ?;
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_information, (information, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса update_information в классе About!') 
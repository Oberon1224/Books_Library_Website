#Copyright 2024 Bushuev Dmitrii

from .table import Table
from .data_for_tables.data_book import data_book
from .query_for_tables.query_book import query_create, query_last_row, query_insert
from .query_for_tables.query_book import query_select_all, query_select_path_book, query_select_on_id_book
from .query_for_tables.query_book import query_update_title, query_update_page, query_update_path_book, query_update_path_image
from .query_for_tables.query_book import query_update_id_category, query_update_id_language, query_update_id_year

class Book(Table):
    """ Класс является моделью таблицы book.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы book \n
            :self.query_insert (str): Запрос добавления данных в таблицу book \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы book \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы book \n
            :self.query_last_row (str): Запрос выборки последней записи таблицы book \n
            :self.query_select_path_book (str): Запрос выборки пути к файлу книги по id книги \n
            :self.query_select_on_id_book (str): Запрос выборки данных о книге по id книги \n
            :self.query_update_title (str): Запрос изменения названия книги \n
            :self.query_update_page (str): Запрос изменения количества страниц книги \n
            :self.query_update_path_book (str): Запрос изменения пути к файлу книги \n
            :self.query_update_path_image (str): Запрос изменения пути к изображению книги \n
            :self.query_update_id_category (str): Запрос изменения категории книги\n
            :self.query_update_id_language (str):Запрос изменения языка книги \n
            :self.query_update_id_year (str): Запрос изменения года издания книги

        SQL-запрос создания таблицы book (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS book 
                (id_book INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
                title TEXT NOT NULL,
                page INTEGER NULL,
                path_book TEXT NULL,
                path_image TEXT NULL,
                id_year INTEGER,
                id_language INTEGER,
                id_about INTEGER,
                id_category INTEGER,
                FOREIGN KEY (id_year) REFERENCES year(id_year),
                FOREIGN KEY (id_language) REFERENCES language(id_language),
                FOREIGN KEY (id_about) REFERENCES about(id_about),
                FOREIGN KEY (id_category) REFERENCES category(id_category));

        SQL-запрос (self.query_insert): 
            ..  code-block:: sql

                INSERT INTO book (title,page, path_book, path_image,id_year,
                id_language,id_about,id_category) VALUES(?,?,?,?,?,?,?,?);
                
        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM book;

        SQL-запрос (self.query_last_row): 
            ..  code-block:: sql

                SELECT id_book FROM book ORDER BY id_book DESC;
    """          
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.data_to_db = data_book
        self.query_insert = query_insert
        self.query_select_all = query_select_all
        self.query_last_row = query_last_row
        self.query_select_path_book = query_select_path_book
        self.query_select_on_id_book = query_select_on_id_book
        self.query_update_title = query_update_title
        self.query_update_page = query_update_page
        self.query_update_path_book = query_update_path_book
        self.query_update_path_image = query_update_path_image
        self.query_update_id_category = query_update_id_category
        self.query_update_id_language = query_update_id_language
        self.query_update_id_year = query_update_id_year

    def select_path_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки пути к файлу книги по id книги

            Args:
                id_book (int): id книги

            SQL-запрос (self.query_select_path_book): 
                ..  code-block:: sql

                    SELECT path_book FROM book WHERE id_book = ?;
                    
            Returns:
                :list[list[str]]: Результат выборки
        """ 
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_path_book, (id_book,))
            all_results=self.cursor.fetchall()
            self.close_connect_db()
            return all_results   
        except:
            print('Ошибка выполнения запроса select_path_book в классе Book!') 

    def select_on_id_book(self, id_book: int) -> list[list[str]]:
        """Функция выборки данных о книге по id книги

            Args:
                id_book (int): id книги

            SQL-запрос (self.query_select_on_id_book): 
                ..  code-block:: sql

                    SELECT title, page, path_book, path_image, id_category, 
                    id_language, id_year FROM book WHERE id_book = ?;
                    
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
            print('Ошибка выполнения запроса select_on_id_book в классе Book!') 

    def insert_get_data(self, title: str, page: int, path_book: str, path_image: str,
                         id_year: int, id_language: int, id_about: int, id_category: int) -> None:
        """Функция добавления данных в таблицу book

            Args:
                title (str): Название книги
                page (int): Количество страниц книги
                path_book (str): Путь к файлу книги
                path_image (str): Путь к изображению книги
                id_year (int): id года книги
                id_language (int): id языка книги
                id_about (int): id описания книги
                id_category (int): id категории книги

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                        INSERT INTO book (title,page, path_book, 
                                        path_image, id_year, id_language, 
                                        id_about, id_category) 
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?);
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (title, page, path_book, path_image, id_year, id_language, id_about, id_category))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса insert_get_data в классе Book!') 

    def update_title(self, title: str, id_book: int) -> None:
        """Функция изменения названия книги

            Args:
                title (str): Название книги
                id_book (int): id  книги

            SQL-запрос (self.query_update_title): 
                ..  code-block:: sql

                    UPDATE book SET title = ? WHERE id_book = ?;
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_title, (title, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса update_title в классе Book!') 

    def update_page(self, page: int, id_book: int) -> None:
        """Функция изменения количества страниц книги

            Args:
                page (str): Количество страниц книги
                id_book (int): id  книги

            SQL-запрос (self.query_update_page): 
                ..  code-block:: sql

                    UPDATE book SET page = ? WHERE id_book = ?;
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_page, (page, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()
        except:
            print('Ошибка выполнения запроса update_page в классе Book!') 

    def update_path_book(self, path_book: str, id_book: int) -> None:
        """Функция изменения пути к файлу книги

            Args:
                path_book (str): Путь к файлу книги
                id_book (int): id книги

            SQL-запрос (self.query_update_path_book): 
                ..  code-block:: sql

                    UPDATE book SET path_book = ? WHERE id_book = ?;
        """   
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_path_book, (path_book, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db() 
        except:
            print('Ошибка выполнения запроса update_path_book в классе Book!')             

    def update_path_image(self, path_image: str, id_book: int) -> None:
        """Функция изменения пути к изображению книги

            Args:
                path_image (str): Путь к изображению книги
                id_book (int): id книги

            SQL-запрос (self.query_update_path_image): 
                ..  code-block:: sql

                    UPDATE book SET path_image = ? WHERE id_book = ?;
        """   
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_path_image, (path_image, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса update_path_image в классе Book!')    

    def update_id_year(self, year: str, id_book: int) -> None:
        """Функция изменения года издания книги

            Args:
                year (str): год книги
                id_book (int): id книги

            SQL-запрос (self.query_update_id_year): 
                ..  code-block:: sql

                    UPDATE book SET id_year = (SELECT id_year FROM year 
                                                        WHERE year = ?)  
                    WHERE id_book = ?;
        """  
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_id_year, (year, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()  
        except:
            print('Ошибка выполнения запроса update_id_year в классе Book!') 

    def update_id_language(self, language: str, id_book: int) -> None:
        """Функция изменения языка книги

            Args:
                language (str): язык книги
                id_book (int): id книги

            SQL-запрос (self.query_update_id_language): 
                ..  code-block:: sql

                    UPDATE book SET id_language = (SELECT id_language FROM language 
                                                  WHERE name = ?)  
                    WHERE id_book = ?;
        """  
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_id_language, (language, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db()  
        except:
            print('Ошибка выполнения запроса update_id_language в классе Book!') 

    def update_id_category(self, category: str, id_book: int) -> None:
        """Функция изменения категории книги

            Args:
                category (str): категория книги
                id_book (int): id книги

            SQL-запрос (self.query_update_id_category): 
                ..  code-block:: sql

                    UPDATE book SET id_category = (SELECT id_category FROM category 
                                                    WHERE name = ?)  
                    WHERE id_book = ?;
        """  
        try:
            self.connect_db()
            self.cursor.execute(self.query_update_id_category, (category, id_book))
            self.sqlite_connection.commit()
            self.close_connect_db() 
        except:
            print('Ошибка выполнения запроса update_id_category в классе Book!')                
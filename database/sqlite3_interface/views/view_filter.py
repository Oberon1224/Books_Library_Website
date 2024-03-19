from .view import View
from .query_for_views.query_view_filter import query_create, query_select_for_filter_all
from .query_for_views.query_view_filter import query_select_for_filter_tag_year, query_select_for_filter_tag_language
from .query_for_views.query_view_filter import query_select_for_filter_year_language, query_select_for_filter_tag
from .query_for_views.query_view_filter import query_select_for_filter_language, query_select_for_filter_year


class ViewFilter(View):
    """ Класс является моделью представления filter.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания представления \n
            :self.query_select_for_filter_all (str): Запрос выборки записей представления по критериям тэг, год и язык \n
            :self.query_select_for_filter_tag_year (str): Запрос выборки записей представления по критериям тэг и год \n
            :self.query_select_for_filter_tag_language (str): Запрос выборки записей представления по критериям тэг и язык \n
            :self.query_select_for_filter_year_language (str): Запрос выборки записей представления по критериям язык и год \n
            :self.query_select_for_filter_tag (str): Запрос выборки записей представления по критерию тэг \n
            :self.query_select_for_filter_language (str): Запрос выборки записей представления по критерию язык\n
            :self.query_select_for_filter_year (str): Запрос выборки записей представления по критерию год\n
     
        SQL-запрос создания представления filter (self.create_query): 
            ..  code-block:: sql

                CREATE VIEW IF NOT EXISTS filter AS 
                SELECT  book.id_book, book.title, book.path_book, book.path_image,
                about.information, language.name AS language, year.year,
                category.name, tag.tag_name FROM book  
                INNER JOIN about ON about.id_book = book.id_about
                INNER JOIN language ON language.id_language = book.id_language
                INNER JOIN category ON category.id_category = book.id_category
                INNER JOIN year ON year.id_year = book.id_year
                INNER JOIN list_tags ON list_tags.id_book = book.id_book 
                INNER JOIN tag  ON list_tags.id_tag = tag.id_tag;
                                                
    """       
    def __init__(self, name_db :str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_select_for_filter_all = query_select_for_filter_all
        self.query_select_for_filter_tag_year = query_select_for_filter_tag_year
        self.query_select_for_filter_tag_language = query_select_for_filter_tag_language
        self.query_select_for_filter_year_language = query_select_for_filter_year_language
        self.query_select_for_filter_tag = query_select_for_filter_tag
        self.query_select_for_filter_language = query_select_for_filter_language
        self.query_select_for_filter_year = query_select_for_filter_year

    def select_for_filter_all(self, tag: str, year: int, language: str) -> list[list[str]]:
        """Функция выполняет фильтр по по критериям тэг, год и язык 

        Args:
            tag (str): Заданный тэг
            year (int): Заданный год
            language (str): Заданный язык
        
        SQL-запрос (self.query_select_for_filter_all): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE tag_name LIKE ?  
                AND year LIKE ?  AND language LIKE ?;     
            
        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_all, (tag, year, language))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_all в классе ViewFilter!')  

    def select_for_filter_tag_year(self, tag: str, year: int) -> list[list[str]]:
        """Функция выполняет фильтр по по критериям тэг и год

        Args:
            tag (str): Заданный тэг
            year (int): Заданный год

        SQL-запрос (self.query_select_for_filter_tag_year): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE tag_name LIKE ?  
                AND year LIKE ?;

        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_tag_year, (tag, year))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_tag_year в классе ViewFilter!')  

    def select_for_filter_tag_language(self, tag: str, language: str) -> list[list[str]]:
        """Функция выполняет фильтр по по критериям тэг и язык

        Args:
            tag (str): Заданный тэг
            language (str): Заданный язык

        SQL-запрос (self.query_select_for_filter_tag_language): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE tag_name LIKE ?  
                AND language LIKE ?;    
            
        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_tag_language, (tag, language))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_tag_language в классе ViewFilter!')  
    
    def select_for_filter_year_language(self, language: str, year: int) -> list[list[str]]:
        """Функция выполняет фильтр по по критериям язык и год

        Args:
            language (str): Заданный язык
            year (int): Заданный год

        SQL-запрос (self.query_select_for_filter_year_language): 
            ..  code-block:: sql

                SELECT * FROM search WHERE year LIKE ? 
                AND language LIKE ?;     

        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_year_language, (language, year))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_year_language в классе ViewFilter!')  
    
    def select_for_filter_tag(self, tag: str) -> list[list[str]]:
        """Функция выполняет фильтр по по критерию тэг

        Args:
            tag (str): Заданный тэг

        SQL-запрос (self.query_select_for_filter_tag): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE tag_name LIKE ?; 

        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """        
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_tag, (tag,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_tag в классе ViewFilter!') 

    def select_for_filter_language(self, language: str) -> list[list[str]]:
        """Функция выполняет фильтр по по критерию язык

        Args:
            language (str): Заданный язык

        SQL-запрос (self.query_select_for_filter_language): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE language LIKE ?;

        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """             
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_language, (language,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_language в классе ViewFilter!') 
    
    def select_for_filter_year(self, year: int) -> list[list[str]]:
        """Функция выполняет фильтр по по критерию год

        Args:
            year (int): Заданный год

        SQL-запрос (self.query_select_for_filter_year): 
            ..  code-block:: sql

                SELECT * FROM filter WHERE year LIKE ?;     

        Returns:
            list[list[str]]: Результаты выборки по фильтру
        """               
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_filter_year, (year,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            self.check_thread = False
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_filter_year в классе ViewFilter!') 
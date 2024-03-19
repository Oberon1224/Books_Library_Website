#Copyright 2024 Bushuev Dmitrii


from .view import View
from .query_for_views.query_view_search import query_create, query_select_all, query_select_on_title

class ViewSearch(View):
    """ Класс является моделью представления search.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания представления \n
            :self.query_select_all (str): Запрос выборки всех записей из представления search \n
            :self.query_select_on_title (str): Запрос выборки записей с заданным названием книги

        SQL-запрос создания представления search (self.create_query): 
            ..  code-block:: sql

                CREATE VIEW IF NOT EXISTS search AS 
                SELECT  book.id_book, book.title, book.path_book, 
                book.path_image, about.information, language.name AS language,
                year.year, category.name FROM book  
                INNER JOIN about ON about.id_book = book.id_about
                INNER JOIN language ON language.id_language = book.id_language
                INNER JOIN category ON category.id_category = book.id_category
                INNER JOIN year ON year.id_year = book.id_year;

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM search;
    """        
    def __init__(self, name_db: str) -> None: 
        super().__init__(name_db = name_db)  
        self.create_query = query_create
        self.query_select_all = query_select_all
        self.query_select_on_title = query_select_on_title

    def select_on_title(self, title: str) -> list[list[str]]:
        """Функция выполняет выборку записей по заданному названию книги

        Args:
            title (str): Заданное название книги

        SQL-запрос (self.query_select_on_title): 
            ..  code-block:: sql

                SELECT * FROM search WHERE title LIKE ?;   
            
        Returns:
            list[list[str]]: Результаты поиска
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_on_title,('%' + title + '%',))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results     
        except:
            print('Ошибка выполнения запроса select_on_title в классе ViewSearch!')  
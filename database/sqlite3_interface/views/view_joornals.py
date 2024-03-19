#Copyright 2024 Bushuev Dmitrii


from .view import View
from .query_for_views.query_view_joornals import query_create, query_select_all

class ViewJoornals(View):
    """ Класс является моделью представления joornals_category.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания представления \n
            :self.query_select_all (str): Запрос выборки всех записей категории "Журналы" \n

        SQL-запрос создания представления joornals_category (self.create_query): 
            ..  code-block:: sql

                CREATE VIEW IF NOT EXISTS joornals_category AS 
                SELECT  book.id_book, book.title, book.path_book,
                book.path_image, about.information, language.name AS language,
                year.year, category.name FROM book  
                INNER JOIN about ON about.id_book = book.id_about
                INNER JOIN language ON language.id_language = book.id_language
                INNER JOIN category ON category.id_category = book.id_category
                INNER JOIN year ON year.id_year = book.id_year
                WHERE category.name = 'Журналы'

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM joornals_category;
    """   
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_select_all = query_select_all
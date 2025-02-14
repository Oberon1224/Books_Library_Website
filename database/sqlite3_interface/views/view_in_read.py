#Copyright 2024 Bushuev Dmitrii


from .view import View
from .query_for_views.query_view_in_read import query_create, query_select_all, query_select_for_user

class ViewInRead(View):
    """ Класс является моделью представления state_read.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания представления \n
            :self.query_select_all (str): Запрос выборки всех записей со статусом "На чтении" \n
            :self.query_select_for_user (str): Запрос выборки всех записей представления со статусом "На чтении" для пользователя
            
        SQL-запрос создания представления state_read (self.create_query): 
            ..  code-block:: sql

                CREATE VIEW IF NOT EXISTS state_read AS 
                SELECT  book.id_book, book.title, book.path_book,
                book.path_image, about.information, language.name AS language,
                year.year, category.name, user.id_user, 
                user.login, state.state_name	FROM book 
                INNER JOIN about ON about.id_book = book.id_about
                INNER JOIN language ON language.id_language = book.id_language
                INNER JOIN category ON category.id_category = book.id_category
                INNER JOIN year ON year.id_year = book.id_year
                INNER JOIN list_states ON list_states.id_book = book.id_book
                INNER JOIN state ON list_states.id_state = state.id_state
                INNER JOIN user ON list_states.id_user = user.id_user
                WHERE state.state_name = 'На чтении';

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM state_read;            

                  
    """       
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_select_all = query_select_all
        self.query_select_for_user = query_select_for_user

    def select_for_user(self, login: str) -> list[list[str]]:
        """Функция выполняет выборку записей со статусом "На чтении" для пользователя

        Args:
            title (str): Заданное название книги

        SQL-запрос (self.query_select_for_user): 
            ..  code-block:: sql

                SELECT * FROM state_read WHERE login = ?;  

        Returns:
            list[list[str]]: Результаты выборки
        """
        try:
            self.connect_db()
            self.cursor.execute(self.query_select_for_user,(login,))
            all_results = self.cursor.fetchall()
            self.close_connect_db()
            return all_results     
        except:
            print('Ошибка выполнения запроса select_for_user в классе ViewInRead!')  
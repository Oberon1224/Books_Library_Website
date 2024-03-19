from .table import Table
from .data_for_tables.data_list_notes import data_list_notes
from .query_for_tables.query_list_notes import query_create, query_insert, query_select_all

class ListNotes(Table):
    """ Класс является моделью таблицы list_notes.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.create_query (str): Запрос создания таблицы list_notes \n
            :self.query_insert (str): Запрос добавления данных в таблицу list_notes \n
            :self.data_to_db (list[list[str]]): Тестовые данные для таблицы list_notes \n
            :self.query_select_all (str): Запрос выборки всех записей из таблицы list_notes \n

        SQL-запрос создания таблицы list_notes (self.create_query): 
            ..  code-block:: sql

                CREATE TABLE IF NOT EXISTS list_notes
                (id_list_notes INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
                id_note INTEGER NOT NULL,
                id_book INTEGER NOT NULL,
                id_user INTEGER NOT NULL,
                FOREIGN KEY(id_book) REFERENCES book(id_book),
                FOREIGN KEY(id_user) REFERENCES user(id_user),
                FOREIGN KEY(id_note) REFERENCES note(id_note));

        SQL-запрос (self.query_select_all): 
            ..  code-block:: sql

                SELECT * FROM list_notes;
    """    
    def __init__(self, name_db: str) -> None:
        super().__init__(name_db = name_db)
        self.create_query = query_create
        self.query_insert = query_insert
        self.data_to_db = data_list_notes
        self.query_select_all = query_select_all

    def insert_get_data(self, id_note: int, id_book: int, id_user: int) -> None:
        """Функция добавления данных в таблицу list_notes

            Args:
                id_note (int): id заметки
                id_book (int): id книги
                id_user (int): id пользователя

            SQL-запрос (self.query_insert): 
                ..  code-block:: sql

                    INSERT INTO list_notes(id_note, id_book, id_user) 
                    VALUES (?, ?, ?);
        """    
        try:
            self.connect_db()
            self.cursor.execute(self.query_insert, (id_note, id_book, id_user))
            self.sqlite_connection.commit()
            self.close_connect_db()   
        except:
            print('Ошибка выполнения запроса insert_get_data в классе ListNotes!') 
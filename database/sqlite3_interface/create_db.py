from .tables import*
from .views import*
class CreateDataBase:
    """ Класс предназначен для создания базы данных.

        Args:
            name_db (str): Имя базы данных

        Атрибуты:
            :self.about (str): Объект класса About \n
            :self.author (str): Объект класса Author \n
            :self.book (str): Объект класса Book \n  
            :self.category (str): Объект класса Category \n  
            :self.language (str): Объект класса Language \n
            :self.list_authors (str): Объект класса ListAuthors \n
            :self.list_notes (str): Объект класса ListNotes \n
            :self.list_states (str): Объект класса ListStates \n
            :self.list_tags (str): Объект класса ListTags \n
            :self.note (str): Объект класса Note \n
            :self.state (str): Объект класса State \n
            :self.tag (str): Объект класса Tag \n
            :self.year (str): Объект класса Year \n
            :self.user (str): Объект класса User \n
            :self.view_articles (str): Объект класса ViewArticles \n
            :self.view_books (str): Объект класса ViewBooks \n
            :self.view_end_read (str): Объект класса ViewEndRead \n
            :self.view_favorites (str): Объект класса ViewFavorites \n
            :self.view_in_read (str): Объект класса ViewInRead \n
            :self.view_joornals (str): Объект класса ViewJoornals \n
            :self.view_search (str): Объект класса ViewSearch \n
            :self.view_filter (str): Объект класса ViewFilter
    """    
    def __init__(self,name_db: str) -> None:
        self.about = About(name_db)
        self.author = Author(name_db)
        self.book = Book(name_db)
        self.category = Category(name_db)
        self.language = Language(name_db)
        self.list_authors = ListAuthors(name_db)
        self.list_notes = ListNotes(name_db)
        self.list_states = ListStates(name_db)
        self.list_tags =ListTags(name_db)
        self.note = Note(name_db)
        self.state = State(name_db)
        self.tag = Tag(name_db)
        self.year = Year(name_db)
        self.user = User(name_db)
        self.view_articles = ViewArticles(name_db)
        self.view_books = ViewBooks(name_db)
        self.view_end_read = ViewEndRead(name_db)
        self.view_favorites = ViewFavorites(name_db)
        self.view_in_read = ViewInRead(name_db)
        self.view_joornals = ViewJoornals(name_db)
        self.view_search = ViewSearch(name_db)
        self.view_filter = ViewFilter(name_db)

    def create_tables(self) -> None:
        """ Функция создания таблиц базы данных
        
        """    
        self.author.create()
        self.state.create()
        self.user.create()
        self.category.create()
        self.language.create()
        self.year.create()
        self.note.create()
        self.tag.create()
        self.about.create()
        self.book.create()
        self.list_notes.create()
        self.list_tags.create()
        self.list_authors.create()
        self.list_states.create()

    def create_views(self) -> None:
        """ Функция создания представлений базы данных
        """ 
        self.view_articles.create()
        self.view_books.create()
        self.view_end_read.create()
        self.view_favorites.create()
        self.view_in_read.create()
        self.view_joornals.create()
        self.view_search.create()
        self.view_filter.create()
        
    def insert_data_to_db(self) -> None:
        """ Функция добавления тестовых данных в таблицу
        """ 
        self.author.insert_data()
        self.state.insert_data()
        self.user.insert_data()
        self.category.insert_data()
        self.language.insert_data()
        self.year.insert_data()
        self.note.insert_data()
        self.tag.insert_data()
        self.about.insert_data()
        self.book.insert_data()
        self.list_notes.insert_data()
        self.list_tags.insert_data()
        self.list_authors.insert_data()
        self.list_states.insert_data()

    def insert_minimum_data_to_db(self) -> None:
        """ Функция добавления минимальных данных в таблицу:
                1. Тэги
                2. Язык
                3. Год
                4. Категория
                5. Статус
                6. Пользователь
        """ 
        self.state.insert_data()
        self.year.insert_data()
        self.tag.insert_data()
        self.category.insert_data()
        self.language.insert_data()
        self.user.insert_data()
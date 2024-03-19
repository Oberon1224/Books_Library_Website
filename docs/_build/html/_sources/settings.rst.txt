Настройки приложения (settings) 
===============================
	Основные параметры приложения::
	
		Подключение blueprint к приложению:
		
		app.register_blueprint(style) - отвечает за стили сайта
		app.register_blueprint(change_state)
		app.register_blueprint(select_books) - отвечает за выборку книг различных категорий ("Журналы", "Книги", "Статьи")
		app.register_blueprint(select_books_state)- отвечает за выборку книг различных статусов ("На чтении", "Избранное", "Прочитанное")
		app.register_blueprint(search_filter) - отвечает за выбор книг по фильтру
		app.register_blueprint(book_read) - отвечает за страницу чтения книги
		app.register_blueprint(add_to_database) - отвечает за добавление информации в базу данных
		app.register_blueprint(change_book_information) - отвечает за изменение информации в базе данных
		app.register_blueprint(auth) - отвечает за авторизацию на сайте
		
		Переменные app.config:
		
		app.config['DATABASE'] (str): Имя базы данных
		app.config['ABOUT'] (About): Объект класса About (Таблица about) 
		app.config['AUTHOR'] (Author): Объект класса Author (Таблица author) 
		app.config['BOOK'] (Book): Объект класса Book (Таблица book) 
		app.config['CATEGORY'] (Category): Объект класса Category (Таблица category) 
		app.config['LANGUAGE'] (Language): Объект класса Language (Таблица language) 
		app.config['LIST_AUTHORS'] (ListAuthors): Объект класса ListAuthors (Таблица list_authors)
		app.config['LIST_NOTES'] (ListNotes): Объект класса ListNotes (Таблица list_notes)
		app.config['LIST_STATES'] (ListStates): Объект класса ListStates (Таблица list_states)
		app.config['LIST_TAGS'] (ListTags): Объект класса ListTags (Таблица list_tags)
		app.config['NOTE'] (Note): Объект класса Note (Таблица note)
		app.config['STATE'] (State): Объект класса State (Таблица state)
		app.config['TAG'] (Tag): Объект класса Tag (Таблица tag)
		app.config['YEAR'] (Year): Объект класса Year (Таблица year)
		app.config['USER'] (User): Объект класса User (Таблица user)
		app.config['VIEW_ARTICLES'] (ViewArticles): Объект класса ViewArticles (Представление view_articles)
		app.config['VIEW_BOOKS'] (ViewBooks): Объект класса ViewBooks (Представление view_books)
		app.config['VIEW_END_READ'] (ViewEndRead): Объект класса ViewEndRead (Представление view_end_read)
		app.config['VIEW_IN_READ'] (ViewInRead): Объект класса ViewInRead (Представление view_in_read)
		app.config['VIEW_FAVORITES'] (ViewFavorites): Объект класса ViewFavorites (Представление view_favorites)
		app.config['VIEW_JOORNALS'] (ViewJoornals): Объект класса ViewJoornals (Представление view_joornals)
		app.config['VIEW_SEARCH'] (ViewSearch): Объект класса ViewSearch (Представление search)
		app.config['VIEW_FILTER'] (ViewFilter): Объект класса ViewFilter (Представление filter)
		app.config['CREATE_DATABASE'] (CreateDataBase): Объект класса CreateDataBase
		app.config['SEARCH_TITLE'] (str): Переменная хранящая введенное название книги для поиска (для перехода по страницам)
		app.config['FILTER_YEAR'] (int): Переменная хранящая заданный год издания фильтра (для перехода по страницам)
		app.config['FILTER_TAG'] (str): Переменная хранящая заданный тэг фильтра (для перехода по страницам)
		app.config['FILTER_LANGUAGE'] (str): Переменная хранящая заданный язык фильтра (для перехода по страницам)
		app.config['USER_LOGIN'] (str): Логин пользователя
		app.config['STYLE'] (str): Стиль сайта
		



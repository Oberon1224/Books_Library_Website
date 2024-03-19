query_create = """
    CREATE VIEW IF NOT EXISTS articles_category AS 
    SELECT  book.id_book, book.title, book.path_book, book.path_image,
	about.information, language.name AS language, year.year, category.name FROM book  
    INNER JOIN about ON about.id_book = book.id_about
    INNER JOIN language ON language.id_language = book.id_language
    INNER JOIN category ON category.id_category = book.id_category
	INNER JOIN year ON year.id_year = book.id_year
    WHERE category.name='Статьи'
"""

query_select_for_user = "SELECT * FROM articles_category WHERE login = ?"

query_select_all = "SELECT * FROM articles_category"
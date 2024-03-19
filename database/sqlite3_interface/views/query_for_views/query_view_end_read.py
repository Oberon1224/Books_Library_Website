#Copyright 2024 Bushuev Dmitrii

query_create = """
    CREATE VIEW IF NOT EXISTS state_end_read AS 
    SELECT  book.id_book, book.title, book.path_book, book.path_image,
    about.information, language.name AS language, year.year, category.name,
    user.id_user, user.login, state.state_name	FROM book 
    INNER JOIN about ON about.id_book = book.id_about
    INNER JOIN language ON language.id_language = book.id_language
    INNER JOIN category ON category.id_category = book.id_category
	INNER JOIN year ON year.id_year = book.id_year
	INNER JOIN list_states ON list_states.id_book = book.id_book
	INNER JOIN state ON list_states.id_state = state.id_state
	INNER JOIN user ON list_states.id_user = user.id_user
	WHERE state.state_name = 'Прочитанное'
"""

query_select_for_user = "SELECT * FROM state_end_read WHERE login = ?"

query_select_all = "SELECT * FROM state_end_read"
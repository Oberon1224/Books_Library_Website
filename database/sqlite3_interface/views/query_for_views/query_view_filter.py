query_create = """
    CREATE VIEW IF NOT EXISTS filter AS 
    SELECT  book.id_book, book.title, book.path_book, book.path_image,
	about.information, language.name AS language, year.year, category.name, tag.tag_name FROM book  
    INNER JOIN about ON about.id_book = book.id_about
    INNER JOIN language ON language.id_language = book.id_language
    INNER JOIN category ON category.id_category = book.id_category
	INNER JOIN year ON year.id_year = book.id_year
	INNER JOIN list_tags ON list_tags.id_book = book.id_book 
	INNER JOIN tag  ON list_tags.id_tag = tag.id_tag;
"""
#выбраны все критерии
query_select_for_filter_all = "SELECT * FROM filter WHERE tag_name LIKE ?  AND year LIKE ?  AND language LIKE ?;"
#выбран тэг и год
query_select_for_filter_tag_year = "SELECT * FROM filter WHERE tag_name LIKE ?  AND year LIKE ?;"
#выбран тэг и язык
query_select_for_filter_tag_language = "SELECT * FROM filter WHERE tag_name LIKE ?  AND language LIKE ?;"
#выбран язык и год
query_select_for_filter_year_language = "SELECT * FROM search WHERE year LIKE ? AND language LIKE ?;"
#выбран тэг
query_select_for_filter_tag = "SELECT * FROM filter WHERE tag_name LIKE ?;"
#выбран язык
query_select_for_filter_language = "SELECT * FROM search WHERE language LIKE ?;"
#выбран год
query_select_for_filter_year = "SELECT * FROM search WHERE year LIKE ?;"

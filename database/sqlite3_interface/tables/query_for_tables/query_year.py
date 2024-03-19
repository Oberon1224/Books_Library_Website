#Запрос создания таблицы year
query_create="""
    CREATE TABLE IF NOT EXISTS year
    (id_year INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    year TEXT NULL);
"""
#Запрос добавления данных в таблицу year
query_insert="INSERT INTO year(year) VALUES (?);" 

#Запрос создания таблицы year
query_select_all = "SELECT * FROM year;"

#Запрос выборки id года с заданным годом
query_select_id_by_year = "SELECT id_year FROM year WHERE year = ?;"
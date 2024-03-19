#Запрос создания таблицы user
query_create="""
    CREATE TABLE IF NOT EXISTS user
    (id_user INTEGER  PRIMARY KEY AUTOINCREMENT  NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL);
"""
#Запрос добавления данных в таблицу user
query_insert="INSERT INTO user(login, password) VALUES (?, ?);" 

#Запрос выборки всех записей из таблицы user
query_select_all = "SELECT * FROM user;"

#Запрос выборки id пользователя с заданным логином
query_select_id_on_login = "SELECT id_user FROM user WHERE login = ?;"

#Запрос выборки праоля пользователя с заданным логином
query_select_password_on_login = "SELECT password FROM user WHERE login = ?;"
Основной модуль приложения (main) 
=================================
Основной модуль приложения::

		from settings import*
		import sys
		import database as db

		if __name__ == '__main__':
			args = sys.argv[1:]
			if len(args)  == 3:
				if args[2][-3:] == '.db':
					if args[0] == 'database' and args[1] == '-m':
							database=db.CreateDataBase(args[2])
							database.create_tables()
							database.create_views()
							database.insert_minimum_data_to_db()
					elif args[0] == 'database' and args[1] == '-t':
							database=db.CreateDataBase(args[2])
							database.create_tables()
							database.create_views()
							database.insert_data_to_db()
			else:
				app.run()

		

Команда создания базы данных с минимальным объемом данных::

		python main.py database -m [название базы данных].db

Команда создания базы данных с тестовым объемом данных::

		python main.py database -t [название базы данных].db
		



Версии используемых библиотек:

	.. csv-table:: 
	   :header: "Название", "Версия"
	   :widths: 70, 70

	   "Sphinx", "7.2.6"
	   "sphinx-rtd-theme", "2.0.0"
	   "sphinxcontrib-applehelp", "1.0.8"
	   "sphinxcontrib-devhelp", "1.0.6"
	   "sphinxcontrib-htmlhelp", "2.0.5"
	   "sphinxcontrib-jsmath", "1.0.1"
	   "sphinxcontrib-qthelp", "1.0.7"
	   "sphinxcontrib-serializinghtml", "1.1.10"
	   "blinker", "1.7.0"
	   "certifi", "2024.2.2"
	   "charset-normalizer", "3.3.2"
	   "click", "8.1.7"
	   "colorama", "0.4.6"
	   "distlib", "0.3.8"
	   "filelock", "3.13.1"
	   "Flask", "3.0.2"
	   "idna", "3.6"
	   "importlib_metadata", "7.0.2"
	   "itsdangerous", "2.1.2"
	   "Jinja2", "3.1.3"
	   "MarkupSafe", "2.1.5"
	   "platformdirs", "4.2.0"
	   "requests", "2.31.0"
	   "setuptools", "49.2.1"
	   "urllib3", "2.2.1"
	   "virtualenv", "20.25.1"
	   "Werkzeug", "3.0.1"
	   "zipp", "3.17.0"
	 
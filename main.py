#Copyright 2024 Bushuev Dmitrii
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

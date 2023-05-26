import sys
from psycopg2 import Error
from Application import Application
from MainWindow import MainWindow
from DataBaseQuery import DataBaseQuery

try:
    app = Application(sys.argv)
except (Exception, Error) as error:
    print("CONNECTION:", error)
    if app.connection:
        app.cursor.close()
        app.connection.close()
        print("Соединение с PostgreSQL закрыто")

# Класс запросов
dbq = DataBaseQuery(app.connection, app.cursor)
try:
    # Главное окно
    main_window = MainWindow(dbq)
    main_window.showMaximized()
except BaseException as BE:
    print('FATAL ERROR:', BE)

result = app.exec()
sys.exit(result)

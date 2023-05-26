from PyQt5.QtWidgets import QApplication
import psycopg2


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.__connection = psycopg2.connect(user="postgres",
                                             password="Z7578011215z",
                                             host="127.0.0.1",
                                             port="5432",
                                             database="easy_tests")
        # Курсор для выполнения операций с базой данных
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

from UI.Ui_ListSearch import Ui_ListSearch
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from psycopg2 import Error



class ListSearch(QWidget, Ui_ListSearch):
    def __init__(self, main_window, data_base, group_user, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__main_window = main_window
        self.__db = data_base
        self.__group_user = group_user
        self.working_data_on_tests = None
        # ________________________________

        # Функции________________________________
        self.__fill_table()
        self.__set_action()
        # ________________________________

    def __fill_table(self):
        """
        Заполнение таблиц 'Тесты' и 'Уроки'.
        :return:
        """
        # Получение рабочих данных по таблицам 'тесты' и 'уроки'
        try:
            self.working_data_on_tests = self.__db.working_data_on_tests(self.__group_user)
            self.working_data_on_lessons = self.__db.working_data_on_lessons(self.__group_user)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)
        # заполнение таблицы 'тесты'
        if self.working_data_on_tests != 1:
            numcols = 4
            numrows = len(self.working_data_on_tests)
            self.test_table_widget.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):
                    self.test_table_widget.setItem(row, column,
                                                   QTableWidgetItem(str(self.working_data_on_tests[row][column + 3])))
        else:
            return
        # заполнение таблицы 'уроки'
        if self.working_data_on_lessons != 1:
            numcols = 1
            numrows = len(self.working_data_on_lessons)
            self.lessons_table_widget.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):
                    self.lessons_table_widget.setItem(row, column,
                                                      QTableWidgetItem(
                                                          str(self.working_data_on_lessons[row][column + 1]
                                                              )
                                                      ))
        else:
            return

    def __set_action(self):
        self.start_lesson_push_button.clicked.connect(self.__open_lesson)

    def __fill_list_lessons(self):
        pass

    def __open_lesson(self):
        lesson_id = 1
        self.__main_window.open_lesson(lesson_id)
        self.hide()

    def __open_testing(self):
        pass

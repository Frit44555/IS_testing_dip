from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_Analysis import Ui_Analysis
from psycopg2 import Error

from src.for_admin.StatisticTestForAdmin import StatisticTestForAdmin


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_list_users()
        self.__fill_list_test()
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        self.show_result_test_button.clicked.connect(self.__show_statistic_test)

    def __fill_list_users(self):
        """
        Заполняет список пользователей
        """
        try:
            self.__results_all = self.__db.get_results_all()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__results_all == 1:
            return

        self.result_user_list_widget.clear()
        for row in self.__results_all:
            # ID результата, ID пользователя, ID теста, массив ответов, время начала, время конца, коммент админа,
            # коммент пользователя, статус проверки
            elem_list = ''
            elem_list += 'Номер: ' + str(row[0]) + ' | '
            elem_list += 'ID пользователя: ' + str(row[1]) + ' | '
            elem_list += 'Тест: ' + str(row[2]) + ' | '
            elem_list += 'Начал: ' + str(row[4])[:-7] + ' | '
            elem_list += 'Закончил: ' + str(row[5])[:-7] + ' | '

            self.result_user_list_widget.addItem(elem_list)

    def __fill_list_test(self):
        """
        Заполняет список статистики тестов
        """
        try:
            self.__tests_all = self.__db.ger_tests_all()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__tests_all == 1:
            return

        self.result_test_list_widget.clear()
        for row in self.__tests_all:
            # ID теста, массив вопросов, ID тега, название, тип, количество тестов, время выполнения, примечание
            elem_list = ''
            elem_list += 'Тест №: ' + str(row[0]) + ' | '
            elem_list += 'Тег №: ' + str(row[2]) + ' | '
            elem_list += 'Название: ' + row[3] + ' | '
            elem_list += 'Тип: ' + row[4] + ' | '
            elem_list += 'Время: ' + str(row[6]) + ' | '
            elem_list += 'Вопросов: ' + str(row[5]) + ' | '

            self.result_test_list_widget.addItem(elem_list)

    def __show_statistic_test(self):
        print(1)
        self.__statistic_test = StatisticTestForAdmin(parent=self)
        self.vertical_layout_graph_result_test.addWidget(self.__statistic_test)

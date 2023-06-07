from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_Analysis import Ui_Analysis
from PyQt5.QtCore import pyqtSlot
from psycopg2 import Error
import numpy as np

from src.for_admin.StatisticTestForAdmin import StatisticTestForAdmin
from src.for_admin.GraphStatisticTest import GraphStatisticTest
from src.ResultUser import ResultUser


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__statistic_test = None
        self.__plot = None
        self.__result_user = None
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_list_users()
        self.__fill_list_test()
        # ________________________________

        # Опции________________________________
        self.show_result_test_button.setEnabled(False)
        self.show_result_user_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        self.show_result_test_button.clicked.connect(self.__show_statistic_test)
        self.result_test_list_widget.clicked.connect(self.__get_index_test)
        self.result_user_list_widget.clicked.connect(self.__get_index_user)
        self.show_result_user_button.clicked.connect(self.__show_statistics_user)

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

    def __get_index_test(self):
        """
        Получение индекса выбранного теста и включение кнопки посмотреть.
        """
        self.show_result_test_button.setEnabled(True)
        self.__index_test = self.result_test_list_widget.selectedIndexes()[0].row()

    def __get_index_user(self):
        """
        Получение индекса выбранного пользователя и включение кнопки посмотреть.
        """
        try:
            self.show_result_user_button.setEnabled(True)
            index = self.result_user_list_widget.selectedIndexes()[0].data()
            start = index.find('|')
            stop = start + index[start + 1:].find('|')
            self.__index_user = int(index[start + 18:stop].strip())
            print(self.__index_user, type(self.__index_user))

        except BaseException as be:
            print(be)

    @pyqtSlot()
    def __show_statistic_test(self):
        """
        Метод добавляет виджеты статистики по тесту на главный виджет.
        """
        # Item выбранного элемента
        test = self.__tests_all[self.__index_test]
        data = self.__calculation_statistic_test(test)

        # график
        if not self.__statistic_test:
            self.__plot = GraphStatisticTest(parent=self, ordinate=data[-1])
            self.vertical_layout_graph_result_test.addWidget(self.__plot)
        else:
            self.__plot.setParent(None)
            self.__plot = None
            self.__plot = GraphStatisticTest(parent=self, ordinate=data[-1])
            self.vertical_layout_graph_result_test.addWidget(self.__plot)

        # статистика
        if not self.__statistic_test:
            self.__statistic_test = StatisticTestForAdmin(parent=self, data=data)
            self.vertical_layout_graph_result_test.addWidget(self.__statistic_test)
        else:
            self.__statistic_test.setParent(None)
            self.__statistic_test = None
            self.__statistic_test = StatisticTestForAdmin(parent=self, data=data)
            self.vertical_layout_graph_result_test.addWidget(self.__statistic_test)

    def __calculation_statistic_test(self, test):
        """
        Метод считает статистику по тесту.
        :param test
        """
        # Необходимые данные для расчётов из списка переданного теста
        test_id = test[0]
        test_name = test[3]
        quantity_quests = len(test[1])
        quantity_quests_in_testing = test[5]

        # выборка данных с БД
        try:
            all_bals_on_test = self.__db.get_sorted_questions(test_id)
            middle_score = self.__db.get_middle_bals_on_test(test_id)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # словарь, где ключ это номер задания, а значение это полученные баллы по этому заданию
        dict_value = dict()
        key = 0  # необходима для получения количества полученных баллов
        for row in all_bals_on_test:
            # заполнение словаря
            if row[0] in dict_value:
                dict_value[row[0]] = dict_value[row[0]] + [row[-2] if row[-1] else 0, ]
            else:
                dict_value[row[0]] = [row[-2] if row[-1] else 0, ]
                key = row[0]

        general_variance = np.var(all_bals_on_test)  # общая дисперсия теста
        quest_variance = 0                           # дисперсия баллов по заданию теста
        general_selection = len(dict_value[key])     # общая выборка, т.е. сколько было получено заданий
        difficulty = []                              # сложность каждого задания
        for lst in dict_value.values():
            quest_variance += np.var(lst)  # подсчёт суммы дисперсий, это числитель формулы
            difficulty.append((len(lst) - lst.count(0)) / general_selection)

        # коэффициент надёжности
        reliability = (quantity_quests_in_testing / (quantity_quests_in_testing - 1)) *  (1 - (quest_variance / general_variance))

        return test_name, quantity_quests, quantity_quests_in_testing, round(middle_score[2], 2), round(reliability, 2), difficulty

    def __show_statistics_user(self):
        """
        Показывает статистику результата пользователя.
        :return None
        """
        print(self.__index_user)
        if self.__result_user:
            self.__result_user.setParent(None)
            self.__result_user = None
            self.__result_user = ResultUser(parent=self, data=self.__db.get_results_user(self.__index_user),
                                            data_base=self.__db)
            self.vertical_layout_graph_result_user.addWidget(self.__result_user)
        else:
            self.__result_user = ResultUser(parent=self, data=self.__db.get_results_user(self.__index_user),
                                            data_base=self.__db)
            self.vertical_layout_graph_result_user.addWidget(self.__result_user)

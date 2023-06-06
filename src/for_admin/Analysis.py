from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_Analysis import Ui_Analysis
from psycopg2 import Error
import numpy as np

from src.for_admin.StatisticTestForAdmin import StatisticTestForAdmin


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__statistic_test = None
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
        # Item выбранного элемента
        index = self.result_test_list_widget.selectedIndexes()[0].row()
        test = self.__tests_all[index]
        data = self.__calculation_statistic_test(test)

        if not self.__statistic_test:
            self.__statistic_test = StatisticTestForAdmin(parent=self, data=data)
            self.vertical_layout_graph_result_test.addWidget(self.__statistic_test)
        else:
            self.__statistic_test.setParent(None)
            self.__statistic_test = None
            self.__statistic_test = StatisticTestForAdmin(parent=self, data=data)
            self.vertical_layout_graph_result_test.addWidget(self.__statistic_test)

    def __calculation_statistic_test(self, test):
        try:
            test_id = test[0]
            test_name = test[3]
            quantity_quests = len(test[1])
            quantity_quests_in_testing = test[5]

            try:
                all_bals_on_test = self.__db.get_sorted_questions(test_id)
                middle_score = self.__db.get_middle_bals_on_test(test_id)
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

            dict_value = dict()
            key = 0
            for row in all_bals_on_test:
                if row[0] in dict_value:
                    dict_value[row[0]] = dict_value[row[0]] + [row[-2] if row[-1] else 0, ]
                else:
                    dict_value[row[0]] = [row[-2] if row[-1] else 0, ]
                    key = row[0]

            general_variance = np.var(all_bals_on_test)
            quest_variance = 0
            general_selection = len(dict_value[key])
            difficulty = []
            middle_score = []
            for lst in dict_value.values():
                quest_variance += np.var(lst)
                difficulty.append((len(lst) - lst.count(0)) / general_selection)
                temp_true = [i for i in lst if i]
                middle_score.append(sum(temp_true) / len(temp_true))

            reliability = quantity_quests_in_testing / (quantity_quests_in_testing - 1) * \
                          (1 - (quest_variance / general_variance))

            midle_difficulty_test = sum(difficulty) / len(difficulty)

            difference = dict()
            for i in range(len(difficulty)):





            return test_name, quantity_quests, quantity_quests_in_testing, str(round(middle_score[2], 2)), reliability
        except BaseException as be:
            print(be)



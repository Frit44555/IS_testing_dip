from PyQt5.QtWidgets import QWidget
from psycopg2 import Error
from UI.Ui_ResultUser import Ui_ResultUser
from StatisticTestForUser import StatisticTestForUser


class ResultUser(QWidget, Ui_ResultUser):
    def __init__(self, data, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__data = data
        self.__db = data_base
        self.__statistic_test_for_user = None
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_result_list()
        # ________________________________

    def __set_action(self):
        self.show_result_push_button.clicked.connect(self.__draw_statistics)

    def __fill_result_list(self):
        """
        Заполняет список пройденных тестов.
        :return None
        """
        try:
            for row in self.__data:
                elem_lest = ''
                test = self.__db.get_name_time_type_note_on_test(row[2])
                if test == 1:
                    continue

                elem_lest += 'Номер: ' + str(row[0]) + ' | '
                elem_lest += 'Название теста: ' + test[0] + ' | '
                elem_lest += 'Выполнил: ' + str(row[5])[:-7] + ' | '

                self.result_list_widget.addItem(elem_lest)

        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

    def __draw_statistics(self):
        """
        Показывает статистику результата
        :return None
        """
        try:
            # Item выбранного элемента
            index = self.result_list_widget.selectedIndexes()[0]
            # Строка выбранного элемента
            st = index.data()
            result_id = int(st[7:st.find('|')].strip())
            data = self.__statistic(result_id)
            self.__statistic_test_for_user = StatisticTestForUser(data=data, parent=self)
            self.result_vertical_layout.addWidget(self.__statistic_test_for_user)

        except BaseException as error:
            # Вызвать QMessageBox!!!
            print(error)

    def __statistic(self, result_id):
        test_name = None
        score = None
        correct_quest = None
        wrong_quest = None
        time_to_completion = None
        middle_score = None

        answer_user = self.__db.get_answers(result_id)

        return test_name, score, correct_quest, wrong_quest, time_to_completion, middle_score

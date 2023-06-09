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

        # Методы________________________________
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
        if self.__data == 1:
            return
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
            one_separator = st.find('|')
            result_id = int(st[7: one_separator].strip())
            test_name = st[one_separator+17: st.find('|', one_separator+1)].strip()
            data = self.__statistic(result_id, test_name)

            if not self.__statistic_test_for_user:
                self.__statistic_test_for_user = StatisticTestForUser(data=data, parent=self)
                self.result_vertical_layout.addWidget(self.__statistic_test_for_user)
            else:
                self.__statistic_test_for_user.setParent(None)
                self.__statistic_test_for_user = None
                self.__statistic_test_for_user = StatisticTestForUser(data=data, parent=self)
                self.result_vertical_layout.addWidget(self.__statistic_test_for_user)

        except BaseException as error:
            # Вызвать QMessageBox!!!
            print(error)

    def __statistic(self, result_id, test_name):
        score = 0
        score_total = 0
        correct_quest = 0
        wrong_quest = 0
        middle_score = None

        test_id_time_to_completion = [(row[2], row[4], row[5]) for row in self.__data if result_id in row]

        time_to_completion = str(test_id_time_to_completion[0][2] - test_id_time_to_completion[0][1])[:-7]

        try:
            answer_user = self.__db.get_answers(result_id)
            questions = self.__db.get_questions(test_id_time_to_completion[0][0])
            middle_score = self.__db.get_middle_bals_on_test(test_id_time_to_completion[0][0])
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        for answer in answer_user:
            for quest in questions:
                # Задание верно
                if answer[3] and answer[1] == quest[0]:
                    score += quest[2]
                    correct_quest += 1
                    break
                # не верно, при этом это одно и то же задания, а не все попавшие в иначе
                elif answer[1] == quest[0]:
                    score_total += quest[2]
                    wrong_quest += 1

        score_total += score

        # print('время', time_to_completion, "ответы", answer_user, "вопросы", questions, "средний балл", middle_score, sep='\n')
        # print('СТАТИСТИКА', 'БАЛЛ =', score, "/", score_total, "Правильных заданий", correct_quest, "Ошибочных заданий", wrong_quest,
        #       " ВРЕМЯ =", time_to_completion, "Средний =",
        #       str(round(middle_score[2], 2)))

        return test_name, str(score), str(score_total), str(correct_quest), str(wrong_quest),\
            time_to_completion, str(round(middle_score[2], 2))

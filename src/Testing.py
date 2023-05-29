from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
import Words as wrd
from psycopg2 import Error
import datetime

# My widgets
from UI.Ui_Testing import Ui_Testing
from quest.QuestOneAnswer import QuestOneAnswer


class Testing(QWidget, Ui_Testing):
    def __init__(self, user_id, test_id, questions, data_base, type_testing, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__user = user_id
        # Типы тестов: 'SCALE', 'FREE RESPONSE', 'MIXED', 'PREDEFINED'
        self.__type_testing = type_testing
        self.__test = test_id
        print()
        self.__db = data_base
        self.__answers = []
        self.__time_start = datetime.datetime.now()

        # Таблица вопросов хранит: ID вопроса, тип вопроса, балл, картинка, вопрос,
        # ответ1, ответ2, ответ3, ответ4, правильный ответ.
        # Типы вопросов: 'ONE ANSWER', 'MANY ANSWERS', 'SCALE', 'FREE RESPONSE'
        self.__questions = questions
        # ________________________________

        # Функции________________________________
        self.__set_action()
        # ________________________________

    def __set_action(self):
        self.complete_push_button.clicked.connect(self.__close)
        self.__assembly_testing()

    @pyqtSlot()
    def __close(self):
        """
        Принудительное завершение тестирования
        :return None
        """
        qm = QMessageBox
        reply = qm.question(self, wrd.testing['close_testing_warning'], wrd.testing['close_testing'], qm.Yes | qm.No)
        # ответ
        if reply == qm.Yes:
            self.__complete_testing()
            self.close()
        else:
            return

    def __assembly_testing(self):
        """
        Собирает тестирование
        :param test:
        :return None
        """
        how_mush_quest = len(self.__questions)
        # Заполнение вкладок TadWidget заданиями
        for i in range(how_mush_quest):
            # Текущий индекс виджета
            index = self.questions_tab_widget.count()
            # виджет который добавиться на вкладку
            tabPage = self.__what_test(i)
            # добавление страницы на вкладку
            self.questions_tab_widget.insertTab(index, tabPage, f"{i + 1}")
            self.questions_tab_widget.setCurrentIndex(index)

        # Установка текущей вкладки в 0, чтобы открывалась первое задание, а не последнее созданное
        self.questions_tab_widget.setCurrentIndex(0)

    def __what_test(self, i):
        """
        Определяет тип задания.
        Возвращает: Объект "задание тестирования".
        :return str
        """
        if self.__questions[i][1] == 'ONE ANSWER':
            return QuestOneAnswer(data=self.__questions[i], parent=self)
        elif self.__questions[i][1] == 'MANY ANSWERS':
            pass
        elif self.__questions[i][1] == 'SCALE':
            pass
        elif self.__questions[i][1] == 'FREE RESPONSE':
            pass

    @pyqtSlot()
    def __complete_testing(self):
        """
        Завершение тестирования.
        В случае принудительного завершения, если не даны все ответы, из общего списка удаляются те задания,
        на которые ответили. Затем список ответов расширяется списком заданий, засчитанных как проваленные и
        вызывается функция заполнения результата.
        В случае если ответы были даны, то просто вызывается функция заполнения результата.
        :return None
        """
        # Длины не будут соответствовать только в там случае, если ответы не были даны не все задания
        if len(self.__answers) != len(self.__questions):
            for i in range(len(self.__answers)):
                for j in range(len(self.__questions)):
                    if self.__answers[i][0] == self.__questions[j][0]:
                        self.__questions.pop(j)
                        break

            self.__answers.extend([(self.__questions[i][0], '0', False) for i in range(len(self.__questions))])
            self.__result()
        else:
            self.__result()

    def add_answer(self, quest_id, answer, correct):
        """
        Добавление ответа в список ответов виджета тестирования.
        Если такой же ответ уже был, то он "перезаписывается".
        :param quest_id:
        :param answer:
        :param correct:
        :return None
        """
        # Изначально список пуст
        if not self.__answers:
            self.__answers.append((quest_id, answer, correct))
        else:
            # был дан ответ и список не пуст
            for i in range(len(self.__answers)):
                # замена уже данного ответа
                if quest_id in self.__answers[i]:
                    self.__answers.pop(i)
                    self.__answers.insert(i, (quest_id, answer, correct))
                    break
            else:
                # такого ответа не было
                self.__answers.append((quest_id, answer, correct))

    def __result(self):
        """
        Сохранение результата
        :return:
        """
        if self.__type_testing == 'PREDEFINED':
            try:
                # Запись и получение ID ответов
                temp_answer_id = []
                for i in range(len(self.__answers)):
                    id_answer = self.__db.create_answer(self.__answers[i][0], self.__answers[i][1], self.__answers[i][2])
                    if id_answer == 1:
                        return 1
                    else:
                        temp_answer_id.append(id_answer)

                # Время окончания теста и запись результата
                time_stop = datetime.datetime.now()
                self.__db.create_result(user_id=self.__user, test_id=self.__test, answer_id=temp_answer_id,
                                        time_start=self.__time_start, time_finish=time_stop, verified=True)

                # Коммиты ответом и результата
                self.__db.connection.commit()
                self.__db.connection.commit()

            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

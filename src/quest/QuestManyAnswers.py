from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
import random

# My widgets
from UI.ui_quest.Ui_QuestManyAnswers import Ui_QuestManyAnswers
from src.quest.StatusAnswerWidget import StatusAnswerWidget
import src.Words as wrd


class QuestManyAnswers(QWidget, Ui_QuestManyAnswers):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__data = data
        self.__testing = parent
        # ________________________________

        # Функции________________________________
        self.__fill_quest()
        self.__set_actions()
        # ________________________________

        # Объекты________________________________
        self.__status_answer_widget = StatusAnswerWidget(self)
        self.verticalLayout.addWidget(self.__status_answer_widget)
        # ________________________________

    def __set_actions(self):
        """
        Устанавливает действия кнопкам
        :return None
        """
        self.confirm_push_button.clicked.connect(self.__answered)

    @pyqtSlot()
    def __answered(self):
        """
        При нажатии на кнопку ответить запускается эта функция.
        Вызывает функцию отправки и меняет статус ответа на "Отвеченный".
        Проверяет, отвечал ли пользователь или нет, в случае если не отвечал, то предупредит об этом.
        :return None
        """
        if not self.answer1_check_box.isChecked() \
                and not self.answer2_check_box.isChecked() \
                and not self.answer3_check_box.isChecked() \
                and not self.answer4_check_box.isChecked():
            QMessageBox.about(self, wrd.testing_quest['title'], wrd.testing_quest['text'])
        else:
            self.__status_answer_widget.answered()
            self.__send_answer()

    def __fill_quest(self):
        """
        Заполнение виджета данными. Заполняется вопрос, картинка и четыре ответа.
        :return None
        """
        # Таблица вопросов хранит: ID вопроса, тип вопроса, балл, картинка, вопрос,
        # ответ1, ответ2, ответ3, ответ4, правильный ответ.
        self.question_text_browser.setText(self.__data[4])
        if self.__data[3]:
            self.picture_label.setPixmap()

        # случайное заполнение ответов
        random_list = [5, 6, 7, 8]
        random.shuffle(random_list)
        self.answer1_text_browser.setText(self.__data[random_list[0]])
        self.answer2_text_browser.setText(self.__data[random_list[1]])
        self.answer3_text_browser.setText(self.__data[random_list[2]])
        self.answer4_text_browser.setText(self.__data[random_list[3]])

    def __check_answer(self):
        """
        Функция проверяет, какие ответы были выбраны.
        :return boolean
        """
        answer = ''
        if self.answer1_check_box.isChecked():
            if answer:
                answer += '|' + self.answer1_text_browser.toPlainText()
            else:
                answer = self.answer1_text_browser.toPlainText()

        if self.answer2_check_box.isChecked():
            if answer:
                answer += '|' + self.answer2_text_browser.toPlainText()
            else:
                answer = self.answer2_text_browser.toPlainText()

        if self.answer3_check_box.isChecked():
            if answer:
                answer += '|' + self.answer3_text_browser.toPlainText()
            else:
                answer = self.answer3_text_browser.toPlainText()

        if self.answer4_check_box.isChecked():
            if answer:
                answer += '|' + self.answer4_text_browser.toPlainText()
            else:
                answer = self.answer4_text_browser.toPlainText()

        if answer == self.__data[9]:
            return answer, True
        else:
            return answer, False

    def __send_answer(self):
        """
        Функция отправляет виджету Testing выбранные ответы.
        :return None
        """
        answer_id = self.__data[0]
        answer, correct = self.__check_answer()
        self.__testing.add_answer(answer_id, answer, correct)

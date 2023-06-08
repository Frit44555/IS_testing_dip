from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
import src.Words as wrd

# My widgets
from UI.form_for_admin.ui_quest_form.Ui_QuestOneAnswer import Ui_QuestOneAnswer


class QuestOneAnswer(QWidget, Ui_QuestOneAnswer):
    def __init__(self, root, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__this_type = 'ONE ANSWER'

        # Переменные________________________________
        self.__root = root
        # ________________________________

        # Функции________________________________
        self.__set_actions()
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
        Метод проверяет данные перед отправкой.
        Проверяет, выбран ответ на задание или нет и поле вопроса. В случае если ответа или вопроса
                    нет, то предупредит об этом.
        :return None
        """
        if not self.answer1_radio_button.isChecked() \
                and not self.answer2_radio_button.isChecked() \
                and not self.answer3_radio_button.isChecked() \
                and not self.answer4_radio_button.isChecked():
            QMessageBox.about(self, wrd.creater_testing['answer_not_chosed_title'],
                              wrd.creater_testing['answer_not_chosed_text'])
        else:
            if self.answer1_text_edit.toPlainText().strip() \
                    and self.answer2_text_edit.toPlainText().strip() \
                    and self.answer3_text_edit.toPlainText().strip() \
                    and self.answer4_text_edit.toPlainText().strip():
                self.__send_answer()
            else:
                QMessageBox.about(self, wrd.creater_testing['not_all_filled_title'],
                                  wrd.creater_testing['not_all_filled_text'])

    def __check_answer(self):
        """
        Функция проверяет, какой ответ был выбран.
        :return None
        """
        answer = ''
        if self.answer1_radio_button.isChecked():
            answer = self.answer1_text_edit.toPlainText().strip()
        elif self.answer2_radio_button.isChecked():
            answer = self.answer2_text_edit.toPlainText().strip()
        elif self.answer3_radio_button.isChecked():
            answer = self.answer3_text_edit.toPlainText().strip()
        elif self.answer4_radio_button.isChecked():
            answer = self.answer4_text_edit.toPlainText().strip()

        return answer

    def __send_answer(self):
        """
        Метод отправляет данные виджету CreateTesting.
        :return None
        """
        self.confirm_push_button.setEnabled(False)
        #  тип вопроса, ВОПРОС, балл, картинка, четыре ответа, и правильный ответ.
        question = self.question_text_edit.toPlainText()
        score = 1
        picture = None
        answer1 = self.answer1_text_edit.toPlainText().strip()
        answer2 = self.answer2_text_edit.toPlainText().strip()
        answer3 = self.answer3_text_edit.toPlainText().strip()
        answer4 = self.answer4_text_edit.toPlainText().strip()
        answer = self.__check_answer()
        self.__root.questions = (self.__this_type, question, score, picture, answer1, answer2, answer3, answer4, answer)

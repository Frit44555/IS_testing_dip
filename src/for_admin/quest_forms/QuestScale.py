from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
import src.Words as wrd

# My widgets
from UI.form_for_admin.ui_quest_form.Ui_QuestScale import Ui_QuestScale


class QuestScale(QWidget, Ui_QuestScale):
    def __init__(self, root, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__this_type = 'SCALE'

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
        self.confirm_push_button.clicked.connect(self.__send_answer)

    @pyqtSlot()
    def __answered(self):
        """
        Метод проверяет данные перед отправкой.
        Проверяет, набран ли вопрос на задание или нет, в случае если поле вопроса пустое, то предупредит об этом.
        :return None
        """
        if not self.question_text_edit.toPlainText():
            QMessageBox.about(self, wrd.creater_testing['not_all_filled_title'],
                              wrd.creater_testing['not_all_filled_text'])
        else:
            self.__send_answer()

    def __send_answer(self):
        """
        Метод отправляет данные виджету CreateTesting.
        :return None
        """
        self.confirm_push_button.setEnabled(False)
        #  тип вопроса, ВОПРОС, балл, картинка, четыре ответа, и правильный ответ.
        question = self.question_text_edit.toPlainText()
        picture = None
        self.__root.questions = (self.__this_type, question, None, picture, None, None, None, None, None)

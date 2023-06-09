from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot

# My widgets
from UI.ui_quest.Ui_QuestFreeAnswer import Ui_QuestFreeAnswer
from src.quest.StatusAnswerWidget import StatusAnswerWidget
import src.Words as wrd


class QuestFreeAnswer(QWidget, Ui_QuestFreeAnswer):
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
        Вызывает функцию отправки и меняет статус ответа на "Отвеченный"
        Проверяет, отвечал ли пользователь или нет, в случае если не отвечал, то предупредит об этом.
        :return None
        """
        if not self.answer_text_edit.toPlainText():
            QMessageBox.about(self, wrd.testing_quest['title'], wrd.testing_quest['text'])
        else:
            self.__status_answer_widget.answered()
            self.__send_answer(self.answer_text_edit.toPlainText())

    def __fill_quest(self):
        """
        Заполнение виджета данными. Заполняется вопрос и картинка.
        :return None
        """
        # Таблица вопросов хранит: ID вопроса, тип вопроса, балл, картинка, вопрос,
        # ответ1, ответ2, ответ3, ответ4, правильный ответ.
        self.question_text_browser.setText(self.__data[4])
        if self.__data[3]:
            self.picture_label.setPixmap()

    def __send_answer(self, answer):
        """
        Функция отправляет виджету Testing выбранный ответ.
        :return None
        """
        answer_id = self.__data[0]
        self.__testing.add_answer(answer_id, answer)

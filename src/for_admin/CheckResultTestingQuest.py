from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CheckResultTestingQuest import Ui_CheckResultTestingQuest


class CheckResultTestingQuest(QWidget, Ui_CheckResultTestingQuest):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__data = data
        # ________________________________

        # Заполнение полей________________________________
        self.question_text_browser.setText(data[1])
        self.answer_text_browser.setText(data[2])
        # ________________________________

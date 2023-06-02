from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CreateTesting import Ui_CreateTesting
from src.for_admin.CreateTestingTypeQuest import CreateTestingTypeQuest
from src.quest.StatusAnswerWidget import StatusAnswerWidget


class CreateTesting(QWidget, Ui_CreateTesting):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Опции________________________________
        self.create_testing_push_button.setEnabled(False)
        self.close_push_button.setEnabled(False)
        # ________________________________

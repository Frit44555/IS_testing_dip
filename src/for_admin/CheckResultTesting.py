from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CheckResultTesting import Ui_CheckResultTesting
from src.for_admin.CheckResultTestingQuest import CheckResultTestingQuest


class CheckResultTesting(QWidget, Ui_CheckResultTesting):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Методы________________________________
        # ________________________________

        # Опции________________________________
        self.complete_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        # ________________________________

    def __enable_button(self):
        self.complete_button.setEnabled(True)
        self.stop_button.setEnabled(True)

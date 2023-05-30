from PyQt5.QtWidgets import QWidget
from UI.Ui_StatisticTestForUser import Ui_Form


class StatisticTestForUser(QWidget, Ui_Form):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Функции________________________________
        self.__fill_data(data)
        # ________________________________

    def __fill_data(self, data):
        pass

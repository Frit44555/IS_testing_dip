from PyQt5.QtWidgets import QWidget
from UI.Ui_ResultUser import Ui_ResultUser


class ResultUser(QWidget, Ui_ResultUser):
    def __init__(self, user_id, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__user = user_id
        self.__db = data_base
        # ________________________________

    def __filling_result_list(self):
        """
        Заполняет список пройденных тестов.
        :return None
        """
        pass

    def __draw_statistics(self):
        """
        Показывает статистику результата
        :return None
        """
        pass

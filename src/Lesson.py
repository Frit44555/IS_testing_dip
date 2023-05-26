from PyQt5.QtWidgets import QWidget
from UI.Ui_Lesson import Ui_Lesson


class Lesson(QWidget, Ui_Lesson):
    def __init__(self, data_base, lesson_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__lesson_id = lesson_id
        # ________________________________

        # Функции________________________________
        self.__fill_content()
        # ________________________________

    def __fill_content(self):
        pass

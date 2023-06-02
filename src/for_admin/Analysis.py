from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_Analysis import Ui_Analysis


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

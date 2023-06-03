from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.dialog_admin.Ui_CreateGroup import Ui_Ui_CreateGroup


class CreateGroup(QWidget, Ui_Ui_CreateGroup):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Функции________________________________
        self.__set_action()
        # ________________________________

        # Переменные________________________________
        self.create_group_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.cancel_push_button.clicked.connect(self.close)
        self.add_tag_push_button.clicked.connect(self.__add_tag)
        self.remove_tag_push_button_3.clicked.connect(self.__remove_tag)

    def __add_tag(self):
        self.create_group_push_button.setEnabled(True)

    def __remove_tag(self):
        self.create_group_push_button.setEnabled(True)

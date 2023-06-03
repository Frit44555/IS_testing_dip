from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.dialog_admin.Ui_ChangeUserGroup import Ui_Ui_ChangeUserGroup


class ChangeUserGroup(QWidget, Ui_Ui_ChangeUserGroup):
    def __init__(self, data_base, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__data = data
        # ________________________________

        # Функции________________________________
        self.__set_action()
        # ________________________________

        # Переменные________________________________
        self.change_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.cancel_push_button.clicked.connect(self.close)
        self.groups_combo_box.currentTextChanged.connect(self.__set_enabled_button)

    def __set_enabled_button(self):
        self.create_tag_push_button.setEnabled(True)



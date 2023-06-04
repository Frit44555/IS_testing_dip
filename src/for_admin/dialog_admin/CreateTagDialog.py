from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.dialog_admin.Ui_CreateTagDialog import Ui_Ui_CreateTagDialog
from psycopg2 import Error


class CreateTagDialog(QWidget, Ui_Ui_CreateTagDialog):
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
        self.create_tag_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        self.cancel_push_button.clicked.connect(self.close)
        self.name_line_edit.textChanged.connect(self.__set_enabled_button)
        self.create_tag_push_button.clicked.connect(self.__create_tag)

    def __set_enabled_button(self):
        """
        Делает кнопку "создать" активной
        """
        self.create_tag_push_button.setEnabled(True)

    def __create_tag(self):
        """
        Метод создаёт тег в БД
        """
        try:
            self.__db.create_tag(self.name_line_edit.text())
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)
        self.__db.connection.commit()
        self.close()

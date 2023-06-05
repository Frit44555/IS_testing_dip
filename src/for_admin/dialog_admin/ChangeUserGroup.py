from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.dialog_admin.Ui_ChangeUserGroup import Ui_Ui_ChangeUserGroup
from psycopg2 import Error


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
        self.__fill_combobox_group()
        # ________________________________

        # Переменные________________________________
        self.change_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        self.cancel_push_button.clicked.connect(self.close)
        self.groups_combo_box.currentTextChanged.connect(self.__set_enabled_button)
        self.change_push_button.clicked.connect(self.__apply)

    def __set_enabled_button(self):
        self.change_push_button.setEnabled(True)
        self.__get_tag()

    def __fill_combobox_group(self):
        """
        Метод заполняет combobox групп
        """
        try:
            # Получение тегов доступных группе и всех тегов
            self.__all_groups = self.__db.get_groups_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # в случае если список будет пустым, то вернётся код 1, и смысла продолжать заполнение нет
        if self.__all_groups == 1:
            return

        for row in self.__all_groups:
            self.groups_combo_box.addItem(row[1])

    def __get_tag(self):
        """
        Метод добавления тега в группу
        """
        index = self.groups_combo_box.currentIndex()
        self.__current_tag = self.__all_groups[index][0]

    def __apply(self):
        """
        Метод завершения изменения
        """
        if self.__current_tag:
            try:
                self.__db.set_user_group(self.__data[0], self.__current_tag)
                self.__db.connection.commit()
                self.close()
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

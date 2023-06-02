from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_ListOfUser import Ui_ListOfUser
from psycopg2 import Error


class ListOfUser(QWidget, Ui_ListOfUser):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__list_users = None
        self.__groups_user = None
        self.__tags_user = None
        # ________________________________

        # Переменные________________________________
        self.__fill_user_list()
        self.__fill_group_list()
        self.__fill_tag_list()
        # ________________________________

    def __fill_user_list(self):
        """
        Заполнение списка назначенных тестов
        :return None
        """
        try:
            self.__list_users = self.__db.get_list_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__list_users == 1:
            return

        for row in self.__list_users:
            # ID пользователя, группу пользователя, логин, имя, фамилию, отчество, дату регистрации примечание
            elem_lest = ''
            elem_lest += 'Login: ' + row[2] + ' | '
            elem_lest += 'Группа: ' + str(row[1]) + ' | '
            elem_lest += 'Имя: ' + row[4] + ' | '
            elem_lest += 'Дата регистрации: ' + str(row[6]) + ' | '

            self.users_list_widget.addItem(elem_lest)

    def __fill_group_list(self):
        try:
            self.__groups_user = self.__db.get_groups_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__groups_user == 1:
            return

        for row in self.__groups_user:
            # ID тега, название
            elem_lest = ''
            elem_lest += 'ID: ' + str(row[0]) + ' | '
            elem_lest += 'Название: ' + row[1] + ' | '

            self.groups_user_list_widget.addItem(elem_lest)


    def __fill_tag_list(self):
        try:
            self.__tags_user = self.__db.get_tags()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__tags_user == 1:
            return

        for row in self.__tags_user:
            # ID тега, название
            elem_lest = ''
            elem_lest += 'ID: ' + str(row[0]) + ' | '
            elem_lest += 'Название: ' + row[1] + ' | '

            self.tags_list_widget.addItem(elem_lest)
